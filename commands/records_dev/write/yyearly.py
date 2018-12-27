import click
import requests
import bs4
import json
import boto3
from records_dev.aws.dynamodb import dynamodb


@click.command()
@click.pass_context
def yyearly(ctx):
    def request_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        return bs4.BeautifulSoup(res.content, "html.parser")

    def link_tail_list(url):
        soup = request_soup(url)
        table = soup.find("table")
        td_player_list = table.find_all('td', class_='lt yjM')
        return [pl.find('a').get('href') for pl in td_player_list]

    def yearly_records(yearly_table):
        yheader = [th.text.replace('|', 'ー') for th in yearly_table.find_all('th')]
        
        ybody_tr = yearly_table.find_all('tr')[1:]
        yearly_records = []
        for year in ybody_tr:
            ybody = [td.text for td in year.find_all('td')]
            if ybody[0] == '2018':
                continue
            # last content have no 'team' value
            if len(ybody) < len(yheader):
                ybody.insert(1, '')
            year_dict = dict(zip(yheader, ybody))
            yearly_records.append(year_dict)
        return yearly_records

    baseurl = 'https://baseball.yahoo.co.jp/'

    for i in range(1,13):

        dynamo = dynamodb('PersonalRecordsTable')

        purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
        hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'

        pit_link_tail_list = link_tail_list(purl)
        hit_link_tail_list = link_tail_list(hurl)

        for ptail in pit_link_tail_list:
            personal_link = baseurl + ptail
            personal_soup = request_soup(personal_link)

            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            personal_year_link = personal_link + '/year'
            personal_year_soup = request_soup(personal_year_link)
            yearly_table = personal_year_soup.find_all('table')
            if len(yearly_table) < 2:
                continue
            
            yearly_records = yearly_records(yearly_table[1])
            dynamo.batch_write_item(name, yearly_records)

        for htail in hit_link_tail_list:
            personal_link = baseurl + htail
            personal_soup = request_soup(personal_link)

            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            personal_year_link = personal_link + '/year'
            personal_year_soup = request_soup(personal_year_link)
            yearly_table = personal_year_soup.find_all('table')
            if len(yearly_table) < 2:
                continue

            yearly_records = yearly_records(yearly_table[1])
            dynamo.batch_write_item(name, yearly_records)

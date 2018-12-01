import click
import requests
import bs4
import json
import boto3


@click.command()
@click.pass_context
def ypersonal(ctx):

    def request_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        return bs4.BeautifulSoup(res.content, "html.parser")

    def link_tail_list(url):
        soup = request_soup(url)
        table = soup.find("table")
        td_player_list = table.find_all('td', class_='lt yjM')
        return [pl.find('a').get('href') for pl in td_player_list]

    baseurl = 'https://baseball.yahoo.co.jp/'

    for i in range(1,13):

        purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
        hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'

        pit_link_tail_list = link_tail_list(purl)
        hit_link_tail_list = link_tail_list(hurl)

        for ptail in pit_link_tail_list:
            personal_link = baseurl + ptail
            personal_soup = request_soup(personal_link)
            tables = personal_soup.find_all('table')
            records_table = tables[1]
            lr_table = tables[6]
            # 0: profile
            # 1: **records
            # 2: *recent records
            # 3/4: *records by teams central/pacific
            # 5: monthly records
            # 6: **left/right
            # 7: field
            # 8: open

            # profile
            personal_year_link = baseurl + ptail + '/year'
            personal_year_soup = request_soup(personal_year_link)
            yearly_tables = personal_year_soup.find_all('table')
            profile_table = yearly_tables[0]

            # yearly records
            yearly_table = yearly_tables[1]
            header = [th.text.replace('|', 'ー') for th in yearly_table.find_all('th')]
            body_tr = yearly_table.find_all('tr')[1:]
            yearly_records = []
            for year in body_tr:
                body = [td.text for td in year.find_all('td')]
                year_dict = dict(zip(header, body))
                yearly_records.append(year_dict)

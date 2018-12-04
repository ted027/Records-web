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

    def extend_array(array):
        new_array = []
        for elem in array:
            elem.replace('（','(').replace('）',')')
            if '(' in elem:
                elem_split =elem.replace(')', '').split('(')
                new_array.extend(elem_split)
            else:
                new_array.append(elem)
        return new_array

    baseurl = 'https://baseball.yahoo.co.jp/'

    for i in range(1,13):

        purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
        hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'

        pit_link_tail_list = link_tail_list(purl)
        hit_link_tail_list = link_tail_list(hurl)

        for ptail in pit_link_tail_list:
            personal_link = baseurl + ptail
            personal_soup = request_soup(personal_link)

            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            tables = personal_soup.find_all('table')
            # 0: profile
            # 1: **records
            # 2: *recent records
            # 3/4: *records by teams central/pacific
            # 5: monthly records
            # 6: **left/right
            # 7: field
            # 8: open

            records_table = tables[1]
            rheader = [th.text for th in records_table.find_all('th')[1:]]
            rbody = [td.text for td in records_table.find_all('td')]
            records = dict(zip(rheader, rbody))
            # write dict records

            lr_table = tables[6]
            # lheader = [th.text for th in lr_table.find_all('th')]
            # lbody = [td.text for td in lr_table.find_all('td')]
            # lr_records = dict(zip(lheader, lbody))

            # profile
            personal_year_link = baseurl + ptail + '/year'
            personal_year_soup = request_soup(personal_year_link)
            yearly_tables = personal_year_soup.find_all('table')
            profile_table = yearly_tables[0]

            raw_pheader = [th.text for th in profile_table.find_all('th')]
            pheader = extend_array(raw_pheader)
            raw_pbody = [td.text for td in profile_table.find_all('td')[1:8]]
            pbody = extend_array(raw_pbody)
            profile = dict(zip(pheader, pbody))
            # write dict profile

            # yearly records
            yearly_table = yearly_tables[1]
            
            yheader = [th.text.replace('|', 'ー') for th in yearly_table.find_all('th')]
            
            ybody_tr = yearly_table.find_all('tr')[1:]
            yearly_records = []
            for year in ybody_tr:
                ybody = [td.text for td in year.find_all('td')]
                if len(ybody) < len(yheader):
                    ybody.insert(1, '')
                year_dict = dict(zip(yheader, ybody))
                yearly_records.append(year_dict)
            # write dict yearly_records

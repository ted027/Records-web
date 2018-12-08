import click
import requests
import bs4
import json
import boto3
import re


@click.command()
@click.pass_context
def yrecords(ctx):
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
            elem.replace('（','(').replace('）',')').replace(')', '').replace('／', '/')
            elem = re.split('[(/]', elem)
            new_array.extend(elem)
        return new_array

    def pitch_records(records_table):
        # [1:] remove '投手成績'
        rheader = [th.text for th in records_table.find_all('th')[1:]]
        rbody = [td.text for td in records_table.find_all('td')]
        return dict(zip(rheader, rbody))

    def lr_pitch_records(lr_table):
        lr_header = [th.text for th in lr_table.find_all('th')]
        r_header = ['対右' + h for h in lr_header]
        l_header = ['対左' + h for h in lr_header]
        
        lr_tr = lr_table.find_all('tr')
        lr_body1 = [td.text for td in lr_tr[-2].find_all('td')]
        if not '右' in lr_body1[0]:
            click.ClickException('cannot find the word that means right records')
        lr_records = dict(zip(r_header, lr_body1[1:]))

        lr_body2 = [td.text for td in lr_tr[-1].find_all('td')]
        if not '左' in lr_body2[0]:
            click.ClickException('cannot find the word that means lenft records')
        lr_records.update(dict(zip(l_header, lr_body2[1:])))
        return lr_records

    baseurl = 'https://baseball.yahoo.co.jp/'

    for i in range(1,13):

        purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
        hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'

        pit_link_tail_list = link_tail_list(purl)
        hit_link_tail_list = link_tail_list(hurl)

        for ptail in pit_link_tail_list:
            personal_link = baseurl + ptail
            personal_soup = request_soup(personal_link)

            # personal name
            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            tables = personal_soup.find_all('table')
            if len(tables < 3):
                continue
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

            records = pitch_records(records_table)

            lr_records = lr_pitch_records(lr_table)
            records.update(lr_records)
            # write dict records

        for htail in hit_link_tail_list:
            personal_link = baseurl + htail
            personal_soup = request_soup(personal_link)

            # need to confirm
            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            tables = personal_soup.find_all('table')
            profile_table = tables[0]
            if len(tables < 3):
                continue
            # need to confirm
            # 0: profile
            # 1: **records
            # -1: open

            # records_table = tables[1]
            # lr_table = tables[6]

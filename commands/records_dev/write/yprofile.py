import click
import requests
import bs4
import json
import boto3
import re


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
            elem.replace('（','(').replace('）',')').replace(')', '').replace('／', '/')
            elem = re.split('[(/]', elem)
            new_array.extend(elem)
        return new_array

    def profile_dict(profile_table):
        raw_pheader = [th.text for th in profile_table.find_all('th')]
        # divide insede () contents
        pheader = extend_array(raw_pheader)
        raw_pbody = [td.text for td in profile_table.find_all('td')[1:8]]
        pbody = extend_array(raw_pbody)
        return = dict(zip(pheader, pbody))

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
            profile_table = tables[0]
            # 0: profile
            # 1: **records
            # 2: *recent records
            # 3/4: *records by teams central/pacific
            # 5: monthly records
            # 6: **left/right
            # 7: field
            # 8: open

            profile = profile_dict(profile_table)
            # write dict profile

        for htail in hit_link_tail_list:
            personal_link = baseurl + htail
            personal_soup = request_soup(personal_link)

            # need to confirm
            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            tables = personal_soup.find_all('table')
            profile_table = tables[0]

            profile = profile_dict(profile_table)
            # write dict profile

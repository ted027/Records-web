import click
import requests
import bs4
import json


@click.command()
@click.pass_context
def ypersonal(ctx):

    def link_tail_list(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")

        table = soup.find("table")
        td_player_list = table.find_all('td', class_='lt yjM')
        link_tail_list = [pl.find('a').get('href') for pl in td_player_list]
        return link_tail_list

    baseurl = 'https://baseball.yahoo.co.jp/'

    for i in range(1,13):

        purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
        hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'

        pit_link_tail_list = link_tail_list(purl)
        hit_link_tail_list = link_tail_list(hurl)
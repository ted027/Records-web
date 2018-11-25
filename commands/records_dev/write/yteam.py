import click
import requests
import bs4
import json

@click.command()
@click.pass_context
def yteam(ctx):

    def request_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        return bs4.BeautifulSoup(res.content, "html.parser")

    orderurl = 'https://baseball.yahoo.co.jp/npb/standings/'
    soup = request_soup(orderurl)
import click
import requests
import bs4
import json


@click.command()
@click.pass_context
def ypersonal(ctx):
    baseurl = 'https://baseball.yahoo.co.jp/npb/teams/'

    for i in range(1,13):

        purl = baseurl + str(i) + '/memberlist?type=a'
        hurl = baseurl + str(i) + '/memberlist?type=b'

        pres = requests.get(purl)
        pres.raise_for_status()
        soup = bs4.BeautifulSoup(pres.content, "html.parser")
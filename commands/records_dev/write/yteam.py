import click
import requests
import bs4
import json


@click.command()
@click.pass_context
def yteam(ctx):
    baseurl = 'https://baseball.yahoo.co.jp/npb/teams/'
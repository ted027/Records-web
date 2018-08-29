"""
lambda handler
"""
import os
import sys

import requests
import bs4
import json

def lambda_handler(event, context):
    baseurl = 'http://baseballdata.jp/'
    curl = baseurl + 'ctop'
    cpurl = baseurl + 'cptop'
    purl = baseurl + 'ptop'
    ppurl = baseurl + 'pptop'

    # for c cp p pp
    res = requests.get(curl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, "html.parser")
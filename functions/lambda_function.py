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
    url = curl
    
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, "html.parser")

    trs = soup.find_all("tr")

    for tr in trs:
        ths = tr.find_all("th")
import click
import requests
import bs4
import json


@click.command()
@click.pass_context
def records(ctx):
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

    raw_header = [
        i for i in trs[0].text.replace("\r", "").replace(" ", "").split("\n")
        if i != ""
    ]
    header = raw_header
    del header[17:21]
    del header[2]
    body = trs[1:]

    records_index = []

    for raw_contents in body:
        contents = [
            i for i in raw_contents.text.replace("\r", "").replace(" ", "")
            .split("\n") if i != ""
        ]
        if contents != raw_header:
            del contents[16:20]
            contents[0] = contents[0].split(":")[1]
            records_index.append(contents)

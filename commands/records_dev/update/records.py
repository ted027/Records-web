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

    csurl = baseurl + 'sabr/cNOI'
    cpsurl = baseurl + 'sabr/cHIDARITU'
    psurl = baseurl + 'sabr/pNOI'
    ppsurl = baseurl + 'sabr/pHIDARITU'

    # for c cp p pp
    url = curl
    surl = csurl

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

    records_index = [header]

    for raw_contents in body:
        contents = [
            i for i in raw_contents.text.replace("\r", "").replace(" ", "")
            .split("\n") if i != ""
        ]
        if contents[0] == header[0]:
            continue

        del contents[16:20]
        contents[0] = contents[0].split(':')[1]
        records_index.append(contents)

    sres = requests.get(surl)
    sres.raise_for_status()
    ssoup = bs4.BeautifulSoup(sres.content, "html.parser")

    strs = ssoup.find_all("tr")

    sheader = [
        i for i in strs[0].text.replace("\r", "").replace(" ", "").split("\n")
        if i != ""
    ]
    del sheader[:5]
    records_index[0].extend(sheader)
    sbody = strs[1:]

    for raw_scontents in sbody:
        scontents = [
             i for i in raw_scontents.text.replace("\r", "").replace(" ", "")
            .split("\n") if i != ""
        ]
        sname = scontents[0]
        del scontents[:5]
        if scontents[0] == sheader[0]:
            continue

        sname = sname.split(':')[1]
        for record in records_index:
            if sname != record[0]:
                continue

            record.extend(scontents)

    print(records_index)
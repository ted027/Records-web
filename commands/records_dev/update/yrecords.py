import click
import requests
import bs4
import json


@click.command()
@click.pass_context
def yrecords(ctx):
    baseurl = 'https://baseball.yahoo.co.jp/npb/teams/'

    # team c:1-6 p:7-12
    # f'{baseurl}{team}/memberlist?type={a,b}
    leaguelist = ['ctop', 'cptop', 'ptop', 'pptop']
    sabrlist = ['sabr/cNOI', 'sabr/cHIDARITU', 'sabr/pNOI', 'sabr/pHIDARITU']

    # may change from 1-12 to 1-6&7-12
    for i in range(1,13):

        purl = baseurl + i + '/memberlist?type=a'
        hurl = baseurl + i + '/memberlist?type=b'

        pres = requests.get(purl)
        pres.raise_for_status()
        soup = bs4.BeautifulSoup(pres.content, "html.parser")

        # under here

        trs = soup.find_all("tr")

        raw_header = [
            i
            for i in trs[0].text.replace("\r", "").replace(" ", "").split("\n")
            if i != ""
        ]
        header = raw_header
        if (league == 'ctop' or league == 'ptop'):
            del header[17:21]
            del header[2]
        else:
            header = header[:35]
            del header[27:31]
        body = trs[1:]

        records_index = [header]

        for raw_contents in body:
            contents = [
                i for i in raw_contents.text.replace("\r", "").replace(
                    " ", "").replace("%", "").split("\n") if i != ""
            ]
            if contents[0] == header[0]:
                continue

            if (league == 'ctop' or league == 'ptop'):
                del contents[16:20]
            else:
                contents = contents[:35]
                contents[1] = contents[1][:1]
                del contents[27:31]
            contents[0] = contents[0].split(':')[1]
            records_index.append(contents)

        hres = requests.get(hurl)
        hres.raise_for_status()
        soup = bs4.BeautifulSoup(hres.content, "html.parser")

        strs = ssoup.find_all("tr")

        sheader = [
            i for i in strs[0].text.replace("\r", "").replace(" ", "").split(
                "\n") if i != ""
        ]
        if 'HIDARITU' in sabr:
            sheader = sheader[:19]
            del sheader[:6]
        else:
            del sheader[:5]
        records_index[0].extend(sheader)
        sbody = strs[1:]

        for raw_scontents in sbody:
            scontents = [
                i for i in raw_scontents.text.replace("\r", "").replace(
                    " ", "").replace("%", "").split("\n") if i != ""
            ]
            sname = scontents[0]
            if 'HIDARITU' in sabr:
                scontents = scontents[:19]
                del scontents[:6]
            else:
                del scontents[:5]
            if scontents[0] == sheader[0]:
                continue

            sname = sname.split(':')[1]
            for record in records_index:
                if sname != record[0]:
                    continue

                record.extend(scontents)

        records_dict = {'records': records_index}

        league_head = league.replace('top', '')
        json_path = f'./webui/src/{league_head}records.json'

        f = open(json_path, 'w')
        json.dump(records_dict, f)
        f.close
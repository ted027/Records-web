import click
import requests
import bs4
import json


@click.command()
@click.pass_context
def records(ctx):
    baseurl = 'https://nfljapan.com/'

    leaguelist = ['ctop', 'cptop', 'ptop', 'pptop']
    sabrlist = ['sabr/cNOI', 'sabr/cHIDARITU', 'sabr/pNOI', 'sabr/pHIDARITU']

    def _cut_hitters_main_metrics(contents, head):
        # cut condition value
        if head:
            del contents[2]
        # cut original metrics
        del contents[16:20]
        return contents

    def _cut_pitcher_main_metrics(contents, head):
        # cut connected tr
        contents = contents[:35]
        # cut team name
        if not head:
            contents[1] = contents[1][0]
        # cut original metrics
        del contents[27:31]
        # cut duplicated metrics
        del contents[22:24]
        return contents
    
    def _cut_hitters_sabr_metrics(contents):
        # cut duplicated items
        del contents[:5]
        return contents

    def _cut_pitcher_sabr_metrics(contents):
        # cut original metrics
        contents = contents[:19]
        # cut duplicated items
        del contents[:5]
        return contents

    for (league, sabr) in zip(leaguelist, sabrlist):

        url = baseurl + league
        surl = baseurl + sabr

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")

        trs = soup.find_all("tr")

        raw_header = [
            i
            for i in trs[0].text.replace("\r", "").replace(" ", "").split("\n")
            if i != ""
        ]
        header = raw_header
        if (league == 'ctop' or league == 'ptop'):
            header = _cut_hitters_main_metrics(header, head=True)
        else:
            header = _cut_pitcher_main_metrics(header, head=True)
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
                contents = _cut_hitters_main_metrics(contents, head=False)
            else:
                contents = _cut_pitcher_main_metrics(contents, head=False)
            contents[0] = contents[0].split(':')[1]
            records_index.append(contents)

        sres = requests.get(surl)
        sres.raise_for_status()
        ssoup = bs4.BeautifulSoup(sres.content, "html.parser")

        strs = ssoup.find_all("tr")

        sheader = [
            i for i in strs[0].text.replace("\r", "").replace(" ", "").split(
                "\n") if i != ""
        ]
        if 'HIDARITU' in sabr:
            sheader = _cut_pitcher_sabr_metrics(sheader)
        else :
            sheader = _cut_hitters_sabr_metrics(sheader)
        records_index[0].extend(sheader)
        sbody = strs[1:]

        for raw_scontents in sbody:
            scontents = [
                i for i in raw_scontents.text.replace("\r", "").replace(
                    " ", "").replace("%", "").split("\n") if i != ""
            ]
            sname = scontents[0]
            if 'HIDARITU' in sabr:
                scontents = _cut_pitcher_sabr_metrics(scontents)
            else:
                scontents = _cut_hitters_sabr_metrics(scontents)
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
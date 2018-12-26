import click
import requests
import bs4
import json
import boto3
from records_dev.aws.dynamodb import dynamodb


@click.command()
@click.pass_context
def yrecords(ctx):
    def request_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        return bs4.BeautifulSoup(res.content, "html.parser")

    def link_tail_list(url):
        soup = request_soup(url)
        table = soup.find("table")
        td_player_list = table.find_all('td', class_='lt yjM')
        return [pl.find('a').get('href') for pl in td_player_list]

    def dict_records(records_table):
        # [1:] remove '__成績'
        rheader = [th.text for th in records_table.find_all('th')[1:]]
        rbody = [td.text for td in records_table.find_all('td')]
        return dict(zip(rheader, rbody))

    def chance_records(chance_table):
        chheader_raw = [th.text for th in chance_table.find_all('th')]
        chheader = [chheader_raw[0][:4] + h for h in chheader_raw[1:]]

        chbody = [td.text for td in chance_table.find_all('td')]
        return dict(zip(chheader, chbody))

    def records_by_rl(rl_table,dump_val):
        rl_header = [th.text for th in rl_table.find_all('th')]
        r_header = ['対右' + h for h in rl_header]
        l_header = ['対左' + h for h in rl_header]
        
        rl_tr = rl_table.find_all('tr')
        rl_body1 = [td.text for td in rl_tr[-2].find_all('td')]
        if not '右' in rl_body1[0]:
            click.ClickException('cannot find the word that means right records')
        rl_records = dict(zip(r_header, rl_body1[dump_val:]))

        rl_body2 = [td.text for td in rl_tr[-1].find_all('td')]
        if not '左' in rl_body2[0]:
            click.ClickException('cannot find the word that means lenft records')
        rl_records.update(dict(zip(l_header, rl_body2[dump_val:])))
        return rl_records

    def records_by_count_or_runner(table_by):
        # cut count or runner
        header = [th.text for th in table_by.find_all('th')][1:]
        
        # 2: cut title and header
        body_tr = table_by.find_all('tr')[2:]
        records_by_count_or_runner = {}
        for tr in body_tr:
            body = [td.text for td in tr.find_all('td')]
            records_by_count_or_runner[body[0]] = dict(zip(header, body[1:]))
        return records_by_count_or_runner


    baseurl = 'https://baseball.yahoo.co.jp/'

    for i in range(1,13):

        dynamo = dynamodb('PersonalRecordsTable')

        purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
        hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'

        pit_link_tail_list = link_tail_list(purl)
        hit_link_tail_list = link_tail_list(hurl)

        for ptail in pit_link_tail_list:
            personal_link = baseurl + ptail
            personal_soup = request_soup(personal_link)

            # personal name
            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            tables = personal_soup.find_all('table')
            if len(tables) < 7:
                continue
            records_table = tables[1]
            rl_table = tables[6]
            # 0: profile
            # 1: **records
            # 2: *recent records
            # 3/4: *records by teams central/pacific
            # 5: monthly records
            # 6: **left/right
            # 7: field
            # -1: open

            records = dict_records(records_table)

            # 1: dump '○打'
            records_by_rl = records_by_rl(rl_table, 1)
            records.update(records_by_rl)
            # wip: get year '2018'
            records_item = dynamo.concat_item(name, '2018', records)
            dynamo.put(records_item)

        for htail in hit_link_tail_list:
            personal_link = baseurl + htail
            personal_soup = request_soup(personal_link)

            name = personal_soup.find_all('h1')[-1].text.split('（')[0]

            tables = personal_soup.find_all('table')
            if len(tables) < 10:
                continue
            records_table = tables[1]
            chance_table = tables[2]
            rl_table = tables[7]
            count_table = tables[8]
            runner_table = tables[9]
            # 0: profile
            # 1: **records
            # 2: **chance
            # 3: *recent records
            # 4/5: *records by teams central/pacific
            # 6: monthly records
            # 7: **left/right
            # 8: **count
            # 9: **runner
            # 10: field
            # -1: open

            records = dict_records(records_table)

            chance_records = chance_records(chance_table)
            records.update(chance_records)

            # 2: dump '○投' | '○打席'
            records_by_rl = records_by_rl(rl_table, 2)
            records.update(records_by_rl)

            records_by_count = records_by_count_or_runner(count_table)
            records.update(records_by_count)

            records_by_runner = records_by_count_or_runner(runner_table)
            records.update(records_by_runner)
            # wip: get year '2018'
            records_item = dynamo.concat_item(name, '2018', records)
            dynamo.put(records_item)

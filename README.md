# infrastructure

- Lambda
    - docker image
        - docker pull
        - same...
- Role
    - lambda role
        - upload s3 bucket
- Dynamodb
    - team|name
    - team
- S3
    - web
    - lambda code

# future page
- live scores
- orders(table -> team links)
    - central
    - pacific
- personal records(table -> personal links)
    - central h/p
    - pacific h/p

# py env
```
import click
import requests
import bs4
import json

baseurl = 'https://baseball.yahoo.co.jp/'
i=1
purl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=a'
hurl = baseurl + 'npb/teams/' + str(i) + '/memberlist?type=b'
res = requests.get(purl)
soup = bs4.BeautifulSoup(res.content, "html.parser")

table = soup.find("table")
td_player_list = table.find_all('td', class_='lt yjM')
link_tail_list = [pl.find('a').get('href') for pl in td_player_list]
personal_link = baseurl + link_tail_list[0]

personal_res = requests.get(personal_link)
personal_soup = bs4.BeautifulSoup(personal_res.content, "html.parser")

personal_yres = requests.get(personal_link + '/year')
personal_ysoup = bs4.BeautifulSoup(personal_yres.content, "html.parser")
yearly_tables = personal_ysoup.find_all('table')
profile_table = yearly_tables[0]

yearly_table = yearly_tables[1]
header = [th.text.replace('|', 'ー') for th in yearly_table.find_all('th')]
body_tr = yearly_table.find_all('tr')[1:]
yearly_records = []
for year in body_tr:
    body = [td.text for td in year.find_all('td')]
    year_dict = dict(zip(header, body))
    yearly_records.append(year_dict)


```
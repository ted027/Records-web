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

```
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

# lambda
- PUT
  - personal records
- GET
  - all year records
  - personal records

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
res = requests.get(hurl)
soup = bs4.BeautifulSoup(res.content, "html.parser")

table = soup.find("table")
td_player_list = table.find_all('td', class_='lt yjM')
link_tail_list = [pl.find('a').get('href') for pl in td_player_list]
personal_link = baseurl + link_tail_list[1]

personal_res = requests.get(personal_link)
personal_soup = bs4.BeautifulSoup(personal_res.content, "html.parser")

name = personal_soup.find_all('h1')[-1].text.split('（')[0]
tables = personal_soup.find_all('table')
records_table = tables[1]
rheader = [th.text for th in records_table.find_all('th')[1:]]
rbody = [td.text for td in records_table.find_all('td')]
records = dict(zip(rheader, rbody))

lr_table = tables[6]

personal_yres = requests.get(personal_link + '/year')
personal_ysoup = bs4.BeautifulSoup(personal_yres.content, "html.parser")
yearly_tables = personal_ysoup.find_all('table')
profile_table = yearly_tables[0]

raw_pheader = [th.text for th in profile_table.find_all('th')]
raw_pbody = [td.text for td in profile_table.find_all('td')[1:9]]

yearly_table = yearly_tables[1]
header = [th.text.replace('|', 'ー') for th in yearly_table.find_all('th')]
body_tr = yearly_table.find_all('tr')[1:]
yearly_records = []
for year in body_tr:
    body = [td.text for td in year.find_all('td')]
    if len(body) < len(header):
        body.insert(1, '')
    year_dict = dict(zip(header, body))
    yearly_records.append(year_dict)


```

以下の拡張機能をインストールする

EvilInspector # 全角スペースをわかりやすく出す
Japanese Language Pack for Visual Studio code
Prettier - Code formatter # typescript formatter
Python # python ide for vscode
Swagger Viewer
TSLint # typescript linter
YAML # yaml support
vscode-icons # show icons to each file in vscode

{
    "python.pythonPath": "<python path installed by conda>",
    "restructuredtext.confPath": "${workspaceFolder}/docs",
    "prettier.tabWidth": 4,
    "yaml.schemas": {
        "http://ci-oip-cmn-git-an1c.dev.belem.local/snippets/45/raw": "*template.yml",
        "http://json.schemastore.org/swagger-2.0": ["*swagger.yaml", "*swagger.yml"],
    },
    "python.formatting.provider": "yapf",
    "[python]": {
        "editor.formatOnSave": true
    },
    "[typescript]": {
        "editor.formatOnSave": true,
        "editor.insertSpaces": true,
        "editor.tabSize": 4,
    },
    "files.insertFinalNewline": true,
    "typescript.updateImportsOnFileMove.enabled": "always",
    "javascript.updateImportsOnFileMove.enabled": "always",
}

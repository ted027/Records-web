import click
import requests
import bs4
import json

def create_team_dict(team_Atag, score_tag, dict):
    value_dict = {}
    value_dict['img'] = team_Atag.img.get('src')
    value_dict['link'] = team_Atag.get('href')
    value_dict['score'] = score_tag.text
    dict[team_Atag.text] = value_dict
    return dict

@click.command()
@click.pass_context
def score(ctx):
    baseurl = 'https://nfljapan.com/'

    res = requests.get(baseurl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, "html.parser")

    tables = soup.find_all("table")

    scores_index = []
    for table in tables:
        teams_and_status = table.find_all('a')
        scores = table.find_all('td', class_='score')
        dict = {}
        create_team_dict(teams_and_status[0], scores[0], dict)
        create_team_dict(teams_and_status[2], scores[1], dict)

        status = {}
        status['status'] = teams_and_status[1].text
        status['link'] = teams_and_status[1].get('href')
        dict['status'] = status
        scores_index.extend(dict)

    score_dict = {'scores': scores_index}

    json_path = f'./webui/src/nfl_score.json'

    with open(json_path, 'w') as f:
        json.dump(score_dict, f)
import datetime
import json
import requests
import argparse
import logging
from bs4 import BeautifulSoup
from tabulate import tabulate
from slack_client import slacker

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG,
                    filename='bot.log', filemode='a')

URL = 'https://www.mohfw.gov.in/'
SHORT_HEADERS = ['Sno', 'State', 'In', 'Fr', 'Cd', 'Dt']
FILE_NAME = 'corona_india_data.json'


def save(x):
    with open(FILE_NAME, 'w') as f:
        json.dump(x, f)


def getData(url):
    r = requests.get(url)
    return(r.text)


def extract_contents(row): return [x.text.replace('\n', '') for x in row]


if __name__ == '__main__':

    current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    info = []
    interested_states = "madhya pradesh"
    try:
        myHtmlData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        header = extract_contents(soup.tr.find_all('th'))

        stats = []
        all_rows = soup.find_all("tbody")[9].find_all("tr")
        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            stats.append(stat)

        cur_data = {x[1]: {current_time: x[2:]} for x in stats}
        save(cur_data)
        events_info = ''
        for event in info:
            logging.warning(event)
            events_info += '\n - ' + event.replace("'", "")

        table = tabulate(stats, headers=SHORT_HEADERS, tablefmt='psql')
        slack_text = f'The CoronaVirus Summary for India :\n{events_info}\n```{table}```'
        slacker()(slack_text)
    except Exception as e:
        logging.exception('oops, corono script failed.')
        slacker()(f'Exception occured: [{e}]')

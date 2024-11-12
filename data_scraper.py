import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


def load_urls_from_file(filename):
    urls = []
    with open(filename, 'r') as file:
        for line in file:
            urls.append(line)
    return urls


def parse_html_to_pd(html_url):
    req_response = requests.get(html_url)
    soup = BeautifulSoup(req_response.content, 'html.parser')
    tables = soup.find_all('table')
    car_model = soup.find('title').text.strip()

    tabels_list = []
    for table in tables:
        df = pd.read_html(StringIO(str(table)))[0]
        df.insert(0, "car model", car_model)
        tabels_list.append(df)
    return tabels_list

def to_list_of_dicts(list_of_tables):
    return [table.to_dict(orient='records') for table in list_of_tables]

def to_list_of_str(tabels_list):
    flattened_list = []
    for table in tabels_list:
        for row in table:
            flattened_list.append(str(row))
    return flattened_list

def flattener(urls):
    all_rows = []
    for url in urls:
        tabels_pds = parse_html_to_pd(url)
        tabels_list = to_list_of_dicts(tabels_pds)
        tables_rows = to_list_of_str(tabels_list)
        all_rows.extend(tables_rows)
    return all_rows

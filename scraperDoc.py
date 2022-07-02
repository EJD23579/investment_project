#ScraperDoc
#Credits to O.H for writing the majority of this code: see Github
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

import psycopg2
from configparser import ConfigParser

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as E


HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


#for variable assignment

def get_html_doc(url):
    return requests.get(url, headers=HEADERS)


def get_soup(html):
    return BeautifulSoup(html.text, 'html.parser')


def find_headers(soup):

    table_headers = soup.findAll('div', {"class": "D(tbhg)"})
    if len(table_headers) != 1:
        raise ValueError(f"Should be one set of table header. "
                         f"Received {len(table_headers)}.")

    # composed of singular 'div'
    table_headers = table_headers[0].findAll('div', recursive=False)[0]

    header_data = table_headers.findAll('div', recursive=False)
    header_data = list(map(lambda item: item.get_text(), header_data))

    return header_data


def find_rows(soup):

    table_rows = soup.findAll('div', {"class": "D(tbrg)"})
    if len(table_rows) != 1:
        raise ValueError(f"Should be one set of table rows. "
                         f"Received {len(table_rows)}.")
    table_rows = table_rows[0]
    table_rows = table_rows.findAll('div', recursive=False)

    rows_data = list()
    for row in table_rows:
        columns = row.findAll('div', recursive=False)[0]
        columns = columns.findAll('div', recursive=False)
        row_data = list(map(lambda item: item.get_text(), columns))
        rows_data.append(row_data)

    return rows_data




if __name__ == '__main__':

    ticker = input("Enter ticker: ")

    details = {'1': 'financials', '2': 'balance-sheet', '3': 'cash-flow'}
    details_list = sorted([f'{key}: {value}' for key, value in details.items()])
    detail_key = input(f"{details_list}: ")
    detail = details[detail_key]



    # ticker = sys.argv[1]
    # detail = sys.argv[2]

#REPLACE WITH URL PROGRAMME


    base_url = "https://uk.finance.yahoo.com/quote/"
    query_str = "?p="

    url = f"{base_url}{ticker}/{detail}{query_str}{ticker}"

    print(url)


def expandAll():
        browser = webdriver.Chrome()
        browser.get(url)
        # working!
        cookiesButton = browser.find_element(By.CSS_SELECTOR,'#consent-page > div > div > div > form > div.wizard-body > div.actions.couple > button')

        cookiesButton.click()









        # Net income continuous operations
        html = get_html_doc(url)
        soup = get_soup(html)

        headers = find_headers(soup)
        rows = find_rows(soup)

        df = pd.DataFrame(data=rows, columns=headers)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df)
expandAll()



#REPLACE WITH URL PROGRAMME


html = get_html_doc(url)
soup = get_soup(html)

headers = find_headers(soup)
rows = find_rows(soup)

df = pd.DataFrame(data=rows, columns=headers)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)



val_list = df.values.tolist()

print(val_list)
#four values; positions 2,3,4,5 in each entry, from most recent to least

#Total Rev
totalRevstr = df.iat[0,0]

#Cost of rev
print(df.iat[1,0])


# useful to remember:
# print (val_list[0][0]) prints first position of first list


#prints all titles
for names in val_list:
    print(names[0])



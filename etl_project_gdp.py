import pandas as pd
from glob import glob
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import os
import sqlite3
import numpy as np


# initialisation des données
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
table_attribs = ["Country", "GDP_USD_millions"]
csv_path = 'data/Countries_by_GDP.csv'

def extract(url, table_attribs):
    response = requests.get(url).text
    #if response.status_code == 200:
    soup = BeautifulSoup(response, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = soup.find_all('tbody')
    rows = tables[2].find_all('tr')

    #Extraction des données
    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            if cols[0].find('a') is not None and '_' not in cols[2]:
                    data_dict = {
                        'Country': cols[0].get_text(strip=True),
                        'GDP_USD_billion': cols[1].get_text(strip=True)
                    }
                    df1 = pd.DataFrame(data_dict, index=[0])
                    df = pd.concat([df, df1], ignore_index=True)

    return df


def transform(df):
    GDP_list = df["GDP_USD_millions"].tolist()
    GDP_list = [float("".join(str(x).split(','))) if isinstance(x, str) else x for x in GDP_list if x is not None and x != '']
    GDP_list = [np.round(x/1000,2) for x in GDP_list]
    df["GDP_USD_millions"] = GDP_list
    df=df.rename(columns = {"GDP_USD_millions":"GDP_USD_billions"})
    return df

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


def log_progress(message):
    print(f"[LOG]: {message}")
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

df.to_csv(csv_path, index=False)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('World_Economies.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()











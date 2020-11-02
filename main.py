import csv
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def main():
    '''
    Main function for COVID-19 ETL Pipeline
    '''
    nyt_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
    john_hopkins_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1601844937551r0.6760353603450084'

    nyt_response = pd.read_csv(nyt_url)
    jh_response = pd.read_csv(john_hopkins_url)

    jh_response_us = jh_response[jh_response['Country/Region'] == 'US']

    for nyt_index, nyt_row in nyt_response.iterrows():

        nyt_date = nyt_row['date']

        jh_response_us_current = jh_response_us[jh_response_us['Date'] == nyt_date]
        if not jh_response_us_current.empty:
            print('Date: ' + str(nyt_row['date']), 'Cases: ' + str(nyt_row['cases']), 'Recovered: ' + str(jh_response_us_current['Recovered'].values[0]), 'Deaths: ' + str(nyt_row['deaths']))

main()

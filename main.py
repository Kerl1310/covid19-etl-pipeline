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
    combined_response = []
    combined_response.append(['Date', 'Cases', 'Recovered', 'Deaths'])

    for nyt_index, nyt_row in nyt_response.iterrows():

        date = nyt_row['date']
        jh_response_us_current = jh_response_us[jh_response_us['Date'] == date]
        
        if not jh_response_us_current.empty:
            cases = nyt_row['cases']
            recovered = jh_response_us_current['Recovered'].values[0]
            deaths = nyt_row['deaths']
            
            combined_response.append([date, cases, recovered, deaths])
    print(combined_response)
main()

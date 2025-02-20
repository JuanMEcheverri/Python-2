import datetime
import re
import pandas as pd
import yfinance as yf 

def check_date_format(date_string):
    desired_format = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(desired_format.match(date_string))

def start_date_grater_than_end_date(start_date, end_date):
    return datetime.datetime.strptime(start_date, '%Y-%m-%d') > datetime.datetime.strptime(end_date, '%Y-%m-%d')

def get_financial_data(stock_ticker, star_date, end_date, column_to_extract):
    
    if not isinstance(stock_ticker, str):
        raise TypeError('stock_ticker must be a string')
        
    if not isinstance(star_date, str):
        raise TypeError('star_date must be a string')
    
    if not isinstance(end_date, str):
        raise TypeError('end_date must be a string')
    
    if not check_date_format(star_date):
        raise ValueError('star_date must be in the format YYYY-MM-DD')
    
    if not check_date_format(end_date):
        raise ValueError('end_date must be in the format YYYY-MM-DD')
    
    if not start_date_grater_than_end_date(star_date, end_date):
        raise ValueError('star_date must be grater than end_date')
        
    data = yf.download(stock_ticker, star_date, end_date)
    return data[[column_to_extract]]

if __name__ == "__main__":
    print(get_financial_data('AAPL', '2021-01-01', '2021-01-10', 'Close'))
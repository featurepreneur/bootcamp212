
'''
Created on 

Course work: 
    Template
@author: raja

Source:
    https://github.com/rajacsp/pythonvil/blob/master/currency_converter/currency_converter.py
'''

# Import necessary modules
import requests
from bs4 import BeautifulSoup


def convert_currency(amount, from_currency = 'CAD', to_currency = 'INR'):

    # Collect and parse first page
    page = requests.get(f'https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}')
    # print(page.text)

    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)

    amount_list = soup.find(class_='iGrAod')

    # print(amount_list.text)
    # print(amount_list.text)

    return amount_list.text

def startpy():
    # print('Hey there')

    result = convert_currency(50)
    print(result)

    result = convert_currency(100, 'INR', 'USD')
    print(result)


if __name__ == '__main__':
    startpy()
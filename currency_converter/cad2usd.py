
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



def startpy():
    # print('Hey there')

    # Collect and parse first page
    page = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=100&From=CAD&To=INR')
    # print(page.text)

    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)

    amount_list = soup.find(class_='iGrAod')

    # print(amount_list.text)
    print(amount_list.text)


if __name__ == '__main__':
    startpy()
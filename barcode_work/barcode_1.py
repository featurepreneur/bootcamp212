#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    https://pypi.org/project/python-barcode/
'''

# Import necessary modules
import barcode

def startpy():
    
    #print(barcode.PROVIDED_BARCODES)

    EAN = barcode.get_barcode_class('ean13')

    #print(EAN)

    
    ean = EAN(u'5901234123457')
    print(ean)

    fullname = ean.save('ean13_barcode')
    print(fullname)
    

    # from barcode.writer import ImageWriter
    # ean = EAN(u'5901234123457', writer=ImageWriter())
    # fullname = ean.save('/Users/rajacsp/Desktop/ean13_barcode')
    # print('Saved')

if __name__ == '__main__':
    startpy()
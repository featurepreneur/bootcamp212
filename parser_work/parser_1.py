
'''
Created on 
Course work: 
@author: raja
Source:
    

How to run?
    python parser_1.py --name one --city Toronto
'''

# Import necessary modules
import argparse

def startpy():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True,
                       help='the name of the stack to create.')
    parser.add_argument('--city', type=str, required=True,
                       help='the name of the stack to create.')

    args = parser.parse_args()

    print("Your Name : ", args.name)
    print("Your City : ", args.city)


if __name__ == '__main__':
    startpy()
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:54:09 2015

@author: bridgette
"""

def fizzbuzz():
    """
    Write a program that prints the numbers from 1 to 100. 
    But for multiples of three print “Fizz” instead of the number 
    and for the multiples of five print “Buzz”. 
    For numbers which are multiples of both three and five print “FizzBuzz”.
    """
    for curr_num in range(1, 101):
        output_string = ""
        if curr_num % 3 == 0:
            output_string += "Fizz"
        if curr_num % 5 == 0:
            output_string += "Buzz"
        if output_string == "":
            output_string += str(curr_num)
        print(output_string)
        
        
if __name__ == '__main__':
    fizzbuzz()

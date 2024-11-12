# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:02:38 2024

@author: jasah
"""

number = int(input('Enter an Integer number: '))

for i in range(1, number+1):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    if i % 5 != 0 and i % 3 != 0:
        print(i)

        jasah shamsudheen

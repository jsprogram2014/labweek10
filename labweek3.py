# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:05:47 2024

@author: jasah
"""

pwd1 = input('Enter the new password: ')
pwd2 = input('Enter the new password once again: ')
lowercase = any(letter.islower() for letter in pwd1)
uppercase = any(letter.isupper() for letter in pwd1)
digit = any(letter.isdigit() for letter in pwd1)

# lowercase=pwd1.islower()
# uppercase=pwd1.isupper()
# digit=pwd1.isdigit()

if pwd1 != pwd2:
    print("Passwords must match")
elif len(pwd1) < 8:
    print("Password not complex enough")
elif lowercase != True:
    print("Password not complex enough")
elif uppercase != True:
    print("Password not complex enough")
elif digit != True:
    print("Password not complex enough")
else:
    print("Password matches")


JASAH SHAMSUDHEEN

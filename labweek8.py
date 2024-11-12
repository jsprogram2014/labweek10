# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:16:02 2024

@author: jasah
"""

def farro_shuffle(list_ex,bool_val):
    new_list = []
    if bool_val==True:
        for x in range((len(list_ex))//2):
            new_list.append(list_ex[x])
            new_list.append(list_ex[x + (len(list_ex)//2)])
    elif bool_val==False:
        for x in range((len(list_ex))//2):
            new_list.append(list_ex[x + (len(list_ex)//2)])
            new_list.append(list_ex[x])
            
    return new_list        
    
print(farro_shuffle([1,2,3,4,5,6,7,8], True))
print(farro_shuffle([1,2,3,4,5,6,7,8], False))
print(farro_shuffle([],False))
print(farro_shuffle(['bob','jack'],True))
print(farro_shuffle(['bob','jack'],False))


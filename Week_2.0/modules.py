# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:44:25 2018

@author: TASNUBA
"""
# Finding Mean:

def Average(lst): 
    result = sum(lst) / len(lst)

    print("The mean of list = ", +(result)) 

# Finding Median:
    
def median(thelist):
    sorted_list = sorted(thelist)
    length = len(sorted_list)
    center = length // 2

    if length == 1:
        center_1 = sorted_list[0]
        print ('The median of list = ' + str(center_1))

    elif length % 2 == 0:
        center_2 = sum(sorted_list[center - 1: center + 1]) // 2.0
        print ('The median of list = ' + str(center_2))

    else:
        center_3 = sorted_list[center]
        print ('The median of list = ' + str(center_3))



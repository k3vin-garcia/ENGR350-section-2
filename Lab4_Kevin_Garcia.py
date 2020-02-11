# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 06:48:24 2018

@author: My family
"""
#importing itertools
import itertools

#creating the set
set1 = ['a', 'b', 'c', 'd', 
        'e', 'f' ,'g' ,'h', 
        'i']

#using itertools to perform the 6-permutation
permutation = list(itertools.permutations(set1, 6))

#using nested for loops to iterate through the set until finished
for n in permutation:
    for x in n:
        print(x, end="")
    print()

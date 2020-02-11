# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:03:32 2018

@author: My family
"""
def main():
    list_1 = []
    list_2 = []
    
    list_1_count = int(input("Enter the total amount of numbers in set A: "))
    
    for i in range(1,list_1_count + 1):
        number = int(input("Enter: "))
        list_1.append(number)
    
    list_2_count = int(input("Enter the total amount of numbers in set B: "))
    
    for i in range(1,list_2_count + 1):
        number = int(input("Enter: "))
        list_2.append(number)
    
    print("Set A: ",list_1)
    print("Set B: ",list_2)
    print("The intersection of A and B: " ,intersection(list_1,list_2))
    print("The union of A and B: " ,union(list_1,list_2))
    print("The difference of A and B: " ,difference(list_1,list_2))
    print("The Cartesian Product of A and B: {(" , end="")
    cartesian(list_1,list_2)
    
def union(list_1, list_2,):
    union_A_B = list(set(list_1 + list_2))
    return union_A_B

def difference(list_1,list_2):
    difference_A_B = list(set(list_1) - set(list_2))
    return difference_A_B

def intersection(list_1,list_2):
    intersection_ = set(list_1).intersection(list_2)
    return intersection_

def cartesian(list_1,list_2):
    for a in list_1:
            for b in list_2:
                print(a,", ", b , sep="" , end="")
                if a==list_1[-1] and b==list_2[-1]:
                    print(")}")
                else:
                    print("), (", end = "")
main()
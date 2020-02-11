# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:08:47 2018

@author: My family
"""
def main():
    matrix1 = [[0, 1, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 1]]

    reflexive, irreflexive, symmetric = "No", "No", "No"
    
    antisymmetric, asymmetric, transitive = "No", "No", "No"
    
    if m_is_Reflexive(matrix1):
        reflexive = "Yes"
    if m_is_Irreflexive(matrix1):
        irreflexive = "Yes"
    if m_is_Symmetric(matrix1):
        symmetric = "Yes"
    if m_is_Antisymmetric(matrix1):
        antisymmetric = "Yes"
    if m_is_Asymmetric(matrix1):
        asymmetric = "Yes"
    if m_is_Transitive(matrix1):
        transitive = "Yes"

    for row1 in matrix1:
        for column1 in row1:
            print(column1, end=" ")
        print()       
    print("Reflexive?", reflexive)
    print("Irreflexive?", irreflexive)
    print("Symmetric?", symmetric)
    print("Antisymmetric?", antisymmetric)
    print("Asymetric?", asymmetric)
    print("Transitive?", transitive)

def m_is_Reflexive(matrix1):
    booln=True
    for a in range(len(matrix1)):
        if matrix1[a][a]==0:
            booln=False
    return booln

 
def m_is_Irreflexive(matrix1):
    booln=True
    for a in range(len(matrix1)):
        if matrix1[a][a]==1:
            booln=False
    return booln


def m_is_Symmetric(matrix1):
    booln=True
    for a in range(len(matrix1)):
        for b in range(len(matrix1[0])):
            if (matrix1[a][b]!=matrix1[b][a] and a!=b):
                booln=False
    return booln


def m_is_Antisymmetric(matrix1):
    booln=True
    for a in range(len(matrix1)):
        for b in range(len(matrix1[0])):
            if (a!=b and matrix1[a][b]==1 and matrix1[b][a]==1):
                    booln=False
    return booln


def m_is_Asymmetric(matrix1):
    booln=False
    if m_is_Irreflexive(matrix1) and m_is_Antisymmetric(matrix1):
        booln=True
    return booln


def m_is_Transitive(matrix1):
    booln=True
    for c in range(len(matrix1)):
        for d in range(len(matrix1[0])):
            if matrix1[c][d]==1:
                for e in range(len(matrix1[0])):
                    if 1 not in matrix1[d]:
                        booln=False
                    else:
                        if matrix1[d][e]==1:
                            if matrix1[c][e]!=1:
                                booln=False
    return booln
main()

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:59:27 2022

@author: 
Name - Niteen Balpande
Enr.no-VP21CSEN0100001
Specialization -  CSE
"""
def inv(a, m) :  #invers of funct
    
    m0 = m  ##initialization
    x0 = 0
    x1 = 1

    if (m == 1) :  # rem 1 condition
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1) :
        # q is quotient
        q = a // m  #floor value
        t = m

        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t
    
    # Make x1 positive
    if (x1 < 0) :
        x1 = x1 + m0

    return x1

def findMinX(num, rem, k) :
    # Compute product of all numbers
    prod = 1
    for i in range(0, k) :
        prod = prod * num[i]

    # Initialize result
    result = 0

    # Apply above formula
    for i in range(0,k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp  #pp is noting but solution for moduloo or floor question
    return result % prod
num=[11,16,21,25]
rem=[6,13,9,19]
k=len(num)  # k is size of num[] and rem[].
print("By applying CRT, x is",findMinX(num,rem,k))

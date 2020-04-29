#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:10:47 2020

@author: Trinadh.Singaladevi
"""
import math
def isprime(value):
    #print("sqrt ",int(math.sqrt(value))+1)
    # if value %3 == 0:
    #     return 0
    # step = 4
    # m = int(math.sqrt(value))+1
    # i = 5
    # while i < m:
    #     if value % i == 0:
    #         return 0
    #     step = 6-step
    #     i += step
    #     #print("step",step)
    #     #print("i", i)
    # return 1
        
    for i in range(3,m,2):
        if value % i ==0:
            return 0
    else:
        return 1


T = int(input())

for _ in range(T):
    n = int(input())
    total = 2
    value = 3
    while total != n:
        value += 2
        total += isprime(value)
        #print(value, total)
        
        
    if total == 1:
        value = 2
    print(value)
    
    
#--------------

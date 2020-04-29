#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:21:02 2020

@author: Trinadh.Singaladevi
"""
import math
T = int(input())

for _ in range(T):
    n = int(input())
    factors = []
    while n%2==0:
        factors.append(2)
        n = n//2
    #print("n",n)    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            factors.append(i)
            n  = n//i
            
    if n > 2: 
        factors.append(n)
        
    print(max(factors))
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:56:28 2020

@author: Trinadh.Singaladevi
"""

import math

def GCD(a,b):
    return math.gcd(a,b)

def LCM(a,b):
    return int((a*b)/GCD(a,b))


T = int(input())

for _ in range(T):
    allnumbers = int(input())

    # array of integers
    A=list(range(2,allnumbers+1))
    lcm = 1
    
    for i in A:
        lcm = LCM(lcm,i)
        
    print(lcm)
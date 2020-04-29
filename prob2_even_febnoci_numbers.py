#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:47:50 2020

@author: Trinadh.Singaladevi
"""

T = int(input())

for _ in range(T):
    n = int(input())
    a = 0
    b = 1
    total = 0
    while b<=n:
        if b % 2 ==0:
            total += b
        a,b = b,a+b
        
        
    print(total)
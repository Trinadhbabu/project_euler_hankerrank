#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:14:03 2020

@author: Trinadh.Singaladevi
"""
'''
a+b+c = n
a**2+b**2 = c**2

by solving above two eqations we get
b = (n**2 - 2*a*n)//(2*n - 2*a)
c = n - b - a

'''

import time
T = int(input())

for _ in range(T):

    n = int(input())
    m = -1
    for a in range(3, (n//3)+1):
        b = (n**2 - 2*a*n)//(2*n - 2*a)
        c = n - b - a
        if a**2 + b **2 == c**2:
            if a*b*c > m:
                m = a*b*c
    print(m)



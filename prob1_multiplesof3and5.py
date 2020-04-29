#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:44:42 2020

@author: Trinadh.Singaladevi
"""
import timeit

#Method - 2

start = timeit.default_timer()
n = 20
k = 0
n = n-1
j5 = n//5
j3 = n//3
j15 = n//15

#n*(n+1)/2 gives the sum of first n natural numbers, where as 3 * gives sum of multiples of 3; >> same as division of 2
print(3*j3*(j3+1) + 5 *j5*(j5+1) - 15*j15*(j15+1) >> 1)

print(timeit.default_timer()-start) 














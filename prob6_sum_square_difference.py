#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:52:39 2020

@author: Trinadh.Singaladevi
"""
T = int(input())

for _ in range(T):
    n = int(input())
    
    sumOfSquares = n*(n+1)*(2*n+1)/6
    squaresofsum = (n*(n+1)/2)**2
    
    print(squaresofsum - sumOfSquares)
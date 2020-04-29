#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:48:55 2020

@author: Trinadh.Singaladevi
"""
from operator import mul
from functools import reduce
import itertools
import time


    
#-------------------------    
    start = time.time()
    l1 = []
    i = 999
    n = 800000
    b2 = 100
    max_n = 0
    while i > b2:
        j = i
        while j>b2:
            print("i j",i, j)
            k = i*j
            #print(k)
            if k >n:
                j -=1
                continue
            if k <= max_n:
                break
            if str(k) == str(k)[::-1] and k<n :
                #print(k)
                
                #l1.append(k)
                max_n = k
                print(i,j)
                b2 = j
                break
            j-=1
        i-=1
                    
    print("max = ",max_n)
    end = time.time()-start
 #   ----------------------------------
    




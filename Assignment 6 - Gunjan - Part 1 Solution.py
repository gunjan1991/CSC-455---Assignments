# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:49:07 2016

@author: gunja
"""
# Assignment: 6
# Name: Gunjan Pravinchandra Pandya
# Part: 1

import numpy as np
def ORfunction(x,y):
    
    arr1 = np.array(x)
    arr2 = np.array(y)

    if arr1.shape != arr2.shape:
        return "Invalid input : Matrices not compatible"

    arr3 = np.array(x)

    for x, y in np.ndindex(arr1.shape):
        if arr1[x,y] == False:
            if arr2[x,y] == False:
                arr3[x,y] == False
            else:
                arr3[x,y] = True
        else:
            arr3[x,y] = True
 
    return arr3
        
ORfunction([[True,False],[True, False]],[[True, False],[True, False]])
ORfunction([[True,False],[False, False]],[[False, True],[False, False]])
ORfunction([[True,False,True]],[[False,False]])
ORfunction([[True, False, False], [False, False, False]], [[False, True, True], [True, False, True]])

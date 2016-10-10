# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:47:13 2016

@author: gunjan
"""
#Name: Gunjan Pravinchandra Pandya
#Assignemnt No: 3
#Part: 1

def generateInsert(table,values):
    string = '"INSERT INTO %s VALUES '%table
    string2 = ','.join(values)
    string3 = string+'('+string2+');"'
    return string3
    
generateInsert('Students', ['1', 'Jane', 'A-'])
generateInsert('Phones', ['42', '312-555-1212'])
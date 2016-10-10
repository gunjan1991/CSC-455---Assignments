# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:53:17 2016

@author: gunjan
"""

# Assignment: 6
# Name: Gunjan Pravinchandra Pandya
# Part: 4

import sqlite3
# Open a connection to database
conn = sqlite3.connect("ChaufferDatabase.db") #Should be the database to which table belongs to

# Request a cursor from the database
cursor = conn.cursor()

def generateInsertStatements(table):
    allSelectedRowsTweet = cursor.execute("SELECT * FROM " + table + ";").fetchall()
    
    text_file = open("C:\Gunjan DePaul\CSC 455\Segment 6\InsertStatements.txt", "w")

    for i in range( len( allSelectedRowsTweet ) ):
            text_file.write("%s;\n" % ("INSERT INTO " + table + " VALUES " + str(allSelectedRowsTweet[i])))        
            #print("%s; \n" % ("INSERT INTO " + table + " VALUES " + str(allSelectedRowsTweet[i])))
        

generateInsertStatements('DRIVER')
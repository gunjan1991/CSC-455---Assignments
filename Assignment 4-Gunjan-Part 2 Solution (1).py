# -*- coding: utf-8 -*-
"""
"""
# Assignment: 4
# Name: Gunjan Pravinchandra Pandya
# Part: 2

import sqlite3

cityTable = '''CREATE TABLE CITY
( CHAUFFERCITY VARCHAR2(20) NOT NULL,
  CHAUFFERSTATE VARCHAR2(20),
  CONSTRAINT CHAUCITY_PK PRIMARY KEY(CHAUFFERCITY)
);'''

driverTable = '''CREATE TABLE DRIVER
( LICENSENUMBER INTEGER,
  RENEWED VARCHAR2(20),
  STATUS VARCHAR2(20),
  STATUSDATE DATE,
  DRIVERTYPE VARCHAR2(20),
  LICENSETYPE VARCHAR2(20),
  ORIGINALISSUEDATE DATE,
  NAME VARCHAR2(30),
  SEX VARCHAR2(10),
  CHAUFFERCITY VARCHAR2(30),
  RECORDNUMBER VARCHAR2(20) NOT NULL,
  CONSTRAINT RECNUM_PK PRIMARY KEY(RECORDNUMBER),
  CONSTRAINT CHAUCITY_FK FOREIGN KEY(CHAUFFERCITY) REFERENCES CITY(CHAUFFERCITY)
);'''

# Open a connection to database
conn = sqlite3.connect("ChaufferDatabase.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the tables if we already created it
cursor.execute("DROP TABLE IF EXISTS CITY")
cursor.execute("DROP TABLE IF EXISTS DRIVER")
# Create the table in ChaufferDatabase.db
cursor.execute(cityTable)
cursor.execute(driverTable)
# Open file for reading
fd = open('C:\Gunjan DePaul\CSC 455\Segment 4\Public_Chauffeurs_Short.csv', 'r')
# Read all lines from the file into allLines variable
allLines = fd.readlines()
allLines.pop(0)    # Remove column headings
fd.close()         # Close the file

# For each line in the file
for line in allLines:
    # convert "A,B,C\n" line into ['A', 'B', 'C'] list of values.
    valueList = line.strip().split(',')
    for i in range( len( valueList ) ):
        if valueList[i] == 'NULL':           # To compare with 'NULL' values
            valueList[i] = None              # To convert 'NULL' to None
    newList = [valueList[9],valueList[10]]   # Another newList for CITY Table
    valueList.pop(10)                        # Removing State from valueList for table DRIVER

    cursor.execute("INSERT OR IGNORE INTO CITY VALUES (?,?);", newList)
    cursor.execute("INSERT INTO DRIVER VALUES (?,?,?,?,?,?,?,?,?,?,?);", valueList)

# To check what we inserted into the table
allSelectedRowsCity = cursor.execute("SELECT * FROM CITY;").fetchall()
allSelectedRowsDriver = cursor.execute("SELECT * FROM DRIVER;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRowsCity:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRowsCity)

for eachRow in allSelectedRowsDriver:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRowsDriver)
# Finalize inserts and close the connection to the database
conn.commit()
conn.close()
#
#
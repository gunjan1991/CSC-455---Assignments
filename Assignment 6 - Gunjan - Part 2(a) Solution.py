# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:53:17 2016

@author: gunja
"""

# Assignment: 6
# Name: Gunjan Pravinchandra Pandya
# Part: 2(a)

import sqlite3

tweetTable = '''CREATE TABLE TWEET
( CREATED_AT VARCHAR2(35),
  ID_STR VARCHAR2(50),
  TEXT VARCHAR2(140),
  SOURCE VARCHAR2(100),
  IN_REPLY_TO_USER_ID VARCHAR2(50),
  IN_REPLY_TO_SCREEN_NAME VARCHAR2(50),
  IN_REPLY_TO_STATUS_ID VARCHAR2(50),
  RETWEET_COUNT INTEGER,
  CONTRIBUTORS VARCHAR2(100),
  CONSTRAINT ID_STR_PK PRIMARY KEY (ID_STR)
);'''

# Open a connection to database
conn = sqlite3.connect("Tweetdatabase.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the tables if we already created it
cursor.execute("DROP TABLE IF EXISTS TWEET")
# Create the table in ChaufferDatabase.db
cursor.execute(tweetTable)

conn.commit()
conn.close()
#
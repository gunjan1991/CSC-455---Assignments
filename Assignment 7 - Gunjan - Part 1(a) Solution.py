# -*- coding: utf-8 -*-

# Assignment: 7
# Name: Gunjan Pravinchandra Pandya
# Part: 1(a)

import sqlite3

userTable = '''CREATE TABLE USER
( ID INTEGER,
  NAME VARCHAR2(50),
  SCREEN_NAME VARCHAR2(50),
  DESCRIPTION VARCHAR2(100),
  FRIENDS_COUNT INTEGER,
  CONSTRAINT ID_PK PRIMARY KEY (ID)
);'''

tweetTable = '''CREATE TABLE TWEET
( CREATED_AT VARCHAR2(35),
  ID_STR INTEGER,
  TEXT VARCHAR2(140),
  SOURCE VARCHAR2(100),
  IN_REPLY_TO_USER_ID VARCHAR2(50),
  IN_REPLY_TO_SCREEN_NAME VARCHAR2(50),
  IN_REPLY_TO_STATUS_ID VARCHAR2(50),
  RETWEET_COUNT INTEGER,
  CONTRIBUTORS VARCHAR2(100),
  USER_ID INTEGER,
  CONSTRAINT ID_STR_PK PRIMARY KEY (ID_STR),
  CONSTRAINT USERID_FK FOREIGN KEY (USER_ID) REFERENCES USER(ID)
);'''

# Open a connection to database
conn = sqlite3.connect("Tweetdatabase.db")

# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

# Get rid of the tables if we already created it
cursor.execute("DROP TABLE IF EXISTS TWEET")
cursor.execute("DROP TABLE IF EXISTS USER")
# Create the table in ChaufferDatabase.db
cursor.execute(userTable)
cursor.execute(tweetTable)

conn.commit()
conn.close()
#
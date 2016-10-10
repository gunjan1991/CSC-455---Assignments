/* Assignment No: 7
   Name: Gunjan Pravinchandra Pandya
   Part: 2(a)*/

SELECT ID,NAME FROM USER WHERE FRIENDS_COUNT = (SELECT MAX(FRIENDS_COUNT) FROM USER);
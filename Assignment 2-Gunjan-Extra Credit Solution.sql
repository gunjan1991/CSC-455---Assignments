/*Assignment No.: 2
  Name: Gunjan Pravinchandra Pandya
  Part: Extra Credit Solution*/

/*a.Using the tables you have defined in Part 2, write a SELECT statement that displays the author first name, 
last name and ID for any author whose first name that has an “e” somewhere in the middle of the name.*/

SELECT FIRSTNAME, LASTNAME, AUTHID FROM AUTHORS WHERE FIRSTNAME LIKE '%e%';

/*b.	Using the tables you have defined in Part 2, write a SELECT statement that displays the publisher name, 
address and ID for any publisher whose ID is higher than 17 and order the results in ascending order by ID.*/

SELECT NAME, ADDRESS, PUBID FROM PUBLISHERS WHERE PUBID>17 ORDER BY PUBID;
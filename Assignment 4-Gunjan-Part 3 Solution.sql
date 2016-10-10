/*Assignment No: 4
  Name: Gunjan Pravinchandra Pandya
  Part: 3*/

--1.	Find all the animals (their names) that take less than 1.5 hours to feed.
SELECT AName Animal_Name 
FROM ANIMAL 
WHERE TimeToFeed <1.5;

--2.	Find all the rare animals and sort the query output by feeding time (any direction)
SELECT AName Rare_Animals 
FROM ANIMAL 
WHERE ACategory = 'rare' 
ORDER BY TimeToFeed;

--3.	Find the animal names and categories for animals related to a bear (hint: use the LIKE operator)
SELECT AName Animal_Name, ACategory Animal_Category
FROM ANIMAL 
WHERE AName LIKE '%bear%';

--4.	Return the listings for all animals whose rarity is not specified in the database
SELECT AName Animal_Name 
FROM ANIMAL 
WHERE ACategory IS NULL;

--5.	Find the rarity rating of all animals that require between 1 and 2.5 hours to be fed
SELECT AName Animal_Name, ACategory Animal_Category
FROM ANIMAL 
WHERE TimeToFeed BETWEEN 1 AND 2.5;

--SELECT DISTINCT ACategory Animal_Category FROM ANIMAL WHERE TimeToFeed BETWEEN 1 AND 2.5;

--6.	Find the names of the animals that are related to the tiger and are not common
SELECT AName Animal_Name
FROM ANIMAL 
WHERE AName LIKE '%tiger%' AND ACategory != 'common';

--7.	Find the minimum and maximum feeding time amongst all the animals in the zoo (single query)
SELECT MAX(TimeToFeed) AS Maximum_Feeding_Time, MIN(TimeToFeed) AS Minimum_Feeding_Time 
FROM ANIMAL;

--8.	Find the average feeding time for all the rare animals
SELECT AVG(TimeToFeed) AS Average_Feeding_Time 
FROM ANIMAL 
WHERE ACategory = 'rare';

--9.	Find listings for animals with ID less than 10 and also require more than 2 hours to feed.
SELECT AName 
FROM ANIMAL 
WHERE AID<10 AND TimeToFeed>2;
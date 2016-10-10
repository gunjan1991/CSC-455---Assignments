/* Assignment No: 7
   Name: Gunjan Pravinchandra Pandya
   Part: 4 - Extra Credit*/

--Write a SQL query that finds all animals without a zookeeper assignment using NOT EXISTS with a correlated nested sub-query.
SELECT * 
FROM ANIMAL A 
WHERE NOT EXISTS (SELECT * FROM HANDLES H WHERE H.ANIMALID = A.AID);

--Write a trigger using PL/SQL in Oracle that will ensure that TimeToFeed defaults to at least 0.25 (i.e. if TimeToFeed is less than 0.25, reset it to the value of 0.25)
create or replace trigger animal_before_insert_update
before insert or update on animal for each row
begin
    if :new.timetofeed < 0.25 then
        select 0.25 into :new.timetofeed from dual;
    end if;
end;

--Write a regular expression for identifying Social Security Numbers in the text.
SELECT * 
FROM Strings
WHERE REGEXP_LIKE(String,'^[0-9]{3}-[0-9]{2}-[0-9]{4}$');
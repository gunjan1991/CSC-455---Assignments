/* Assignment No: 5
   Name: Gunjan Pravinchandra Pandya
   Part: 3*/

/* 1.Find the names of all employees who are directly supervised by 'Franklin T Wong'. */
SELECT FNAME||' '||MINIT||' '||LNAME AS EMP_NAME
FROM EMPLOYEE 
WHERE SUPER_SSN = (SELECT E.SSN FROM EMPLOYEE E WHERE E.FNAME || ' ' || E.MINIT || ' ' || E.LNAME = 'Franklin T Wong');

/* 2.For each project, list the project name, project number, and the total hours per week (by all employees) spent on that project.*/
SELECT PNAME AS PROJ_NAME,PNUMBER AS PROJ_NUMBER,SUM(HOURS) AS HOURS_PER_WEEK 
FROM PROJECT P, WORKS_ON W 
WHERE P.PNUMBER = W.PNO GROUP BY P.PNUMBER,P.PNAME 
ORDER BY PNUMBER;

/* 3.For each department, retrieve the department name and the average salary of all employees working in that department.  Order the output by department number 
in ascending order.*/
SELECT DNUMBER AS DEPT_NO, DNAME AS DEPT_NAME, AVG(SALARY) AS AVERAGE_SALARY
FROM DEPARTMENT D, EMPLOYEE E 
WHERE D.DNUMBER = E.DNO 
GROUP BY DNUMBER,DNAME 
ORDER BY D.DNUMBER;

/* 4. Retrieve the average salary of all female employees.*/
SELECT AVG(SALARY) AS AVERAGE_SALARY
FROM EMPLOYEE E 
WHERE SEX = 'F';

/* 5. For each department whose average salary is greater than $43,000, retrieve the department name and the number of employees in that department.*/
SELECT DNAME AS DEPT_NAME,COUNT(E.DNO) AS NUM_OF_EMPLOYEES 
FROM DEPARTMENT D, EMPLOYEE E 
WHERE D.DNUMBER = E.DNO 
GROUP BY DNAME,E.DNO
HAVING AVG(SALARY) > 43000;

/*6. Retrieve the names of employees whose salary is within $22,000 of the salary of the employee who is paid the most in the company (e.g., if the highest 
salary in the company is $82,000, retrieve the names of all employees that make at least $60,000.). */
SELECT E.FNAME || ' ' || E.MINIT || ' ' || E.LNAME AS EMPLOYEE_NAME
FROM EMPLOYEE E 
WHERE (SELECT MAX(SALARY) FROM EMPLOYEE E) - E.SALARY <= 22000;
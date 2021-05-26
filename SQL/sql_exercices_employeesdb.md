```sql

1) A query that will return the total number of employees.
SELECT count(*) FROM employees.employees;



2) A query that will return the total number of departments.
SELECT count(*) FROM employees.departments;



3) A query that will return the total number of employees within each department.

SELECT dept_no, count(*)
FROM employees.dept_emp
GROUP BY 1;



4) A query that will return the 5 employees who worked at the company the longest.

SELECT emp_no, min(hire_date)
FROM employees.employees
GROUP BY 1
ORDER BY 2 ASC
LIMIT 5;




5) A query that will return the 10 newest employees.
SELECT emp_no, hire_date
FROM employees
WHERE year(hire_date) = (SELECT max(year(hire_date)) maxdate FROM employees)
ORDER BY 2 ASC
LIMIT 10;





6) A query that will return the first name, last name, and salary of the top 10 highest paid employees.

SELECT e.first_name, e.last_name, s.salary as sal
FROM employees e
JOIN salaries s
ON s.emp_no = e.emp_no
ORDER BY sal DESC
LIMIT 10;


7) A query that will return the first name, last name, and salary of the highest paid manager.

SELECT fname, lname, max(sal) 
FROM
    (SELECT e.first_name fname, e.last_name lname, s.salary sal
	FROM employees e 
	JOIN salaries s
	ON s.emp_no = e.emp_no
	JOIN titles t
	ON t.emp_no = s.emp_no
	WHERE t.title = "Manager") manager
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 1;




8) A query that will return the first name, last name, and salary of the lowest paid manager.

SELECT fname, lname, min(sal) 
FROM
    (SELECT e.first_name fname, e.last_name lname, s.salary sal
	FROM employees e 
	JOIN salaries s
	ON s.emp_no = e.emp_no
	JOIN titles t
	ON t.emp_no = s.emp_no
	WHERE t.title = "Manager") manager
WHERE sal = 40000
GROUP BY 1, 2;


9) A query that will return the number of employees with each title (ie, Software Engineer)

SELECT title, count(title)
FROM employees.titles
GROUP BY 1;


```

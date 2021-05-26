

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







REDOO!!!!!!!!
5) A query that will return the 10 newest employees.
select first_name, last_name, hire_date
from employees.employees
where year(hire_date) = 2000
order by hire_date asc
limit 10;








6) A query that will return the first name, last name, and salary of the top 10 highest paid employees.

SELECT e.first_name, e.last_name, s.salary as sal
FROM employees e
JOIN salaries s
ON s.emp_no = e.emp_no
ORDER BY sal DESC
LIMIT 10;

7) A query that will return the first name, last name, and salary of the highest paid manager.

8) A query that will return the first name, last name, and salary of the lowest paid manager.

9) A query that will return the number of employees with each title (ie, Software Engineer)
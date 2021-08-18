185. Department Top Three Salaries
with cte as (
select d.name Department,
       e.name Employee,
       Salary,
       dense_rank() over (partition by d.name order by salary desc) dept_rnk
from employee e
join department d
on e.departmentid = d.id
)
select Department,
       Employee,
       Salary
from cte
where dept_rnk <= 3

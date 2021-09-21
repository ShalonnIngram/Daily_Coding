select Department, 
       Employee,
       Salary
from
    (select d.name Department,
           e.name Employee,
           Salary,
           dense_rank() over (partition by d.name order by salary desc) as rnk
    from employee e
    join department d
    on e.departmentid = d.id) sub
where rnk = 1 

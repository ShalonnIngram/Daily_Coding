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





with sal_rank as (
select name,
       salary,
       departmentId,
       dense_rank() over(partition by departmentId order by salary desc) as rnk_sal
from employee
)
select d.name as Department,
       s.name as Employee, 
       s.salary as Salary
from sal_rank s 
left join department d on s.departmentId = d.id
where rnk_sal = 1



1587. Bank Account Summary II
with cte as (
select name, sum(amount) balance
from users u
join transactions t
on u.account = t.account
group by 1
)

select name, balance
from cte
where balance > 10000



178. Rank Scores
select score,
dense_rank() over (order by score desc) `Rank`
from scores


184. Department Highest Salary
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

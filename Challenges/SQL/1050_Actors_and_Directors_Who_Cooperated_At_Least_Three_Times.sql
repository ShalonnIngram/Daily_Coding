h cte as (
    select actor_id, count(actor_id) act_count, director_id, count(director_id) dir_count
    from actordirector
    group by 1
)
select actor_id, director_id
from cte
where act_count >= 3 and dir_count >= 3


OR 


with cte as (
    select *,
    rank() over (partition by actor_id, director_id order by timestamp) as rnk
    from actordirector
)
select actor_id, director_id
from cte
where rnk >= 3

OR

select actor_id, director_id
from actordirector
group by 1, 2
having count(*) >= 3




1076. Project Employees II
with cte as (
    select project_id, sum(employee_id) emp
    from project
    group by 1
)
select project_id 
from cte
having max(emp)



OR


select project_id
from (
    select project_id,
    rank() over(order by count(distinct employee_id) desc) as rnk
    from Project
    group by 1) a
where rnk = 1

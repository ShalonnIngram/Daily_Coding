with cte as (
select p.project_id project_id,
       p.employee_id employee_id,
       experience_years,
       dense_rank() over (partition by project_id order by experience_years desc) rnk
from project p
left join employee e
on p.employee_id = e.employee_id
)
select project_id,
       employee_id
from cte
where rnk = 1

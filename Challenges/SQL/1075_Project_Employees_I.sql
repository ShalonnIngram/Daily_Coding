1075. Project Employees I
select project_id, round(avg(experience_years), 2) average_years
from project p
join employee e
on p.employee_id = e.employee_id
group by 1

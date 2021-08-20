select employee_id,
       count(team_id) over (partition by team_id order by team_id asc) team_size
from employee
group by 1

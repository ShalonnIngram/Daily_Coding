1741. Find Total Time Spent by Each Employee
select event_day day,
       emp_id,
       sum(out_time - in_time) total_time
from employees
group by 1, 2

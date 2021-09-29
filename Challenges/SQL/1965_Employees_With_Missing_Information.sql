select employee_id
from 
    (select * from employees 
    union all
    select * from salaries) t1
group by 1
having count(employee_id) < 2
order by employee_id asc

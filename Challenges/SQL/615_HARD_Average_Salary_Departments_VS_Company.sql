with calc as (
select date_format(pay_date, '%Y-%m') pay_month,
       e.employee_id,
       e.department_id,
       avg(s.amount) over (partition by date_format(pay_date, '%Y-%m'), e.department_id) comp_avg,
       avg(s.amount) over (partition by date_format(pay_date, '%Y-%m')) dept_avg
from salary s
join employee e
on s.employee_id = e.employee_id
)
select distinct pay_month,
       department_id,
       case when dept_avg > comp_avg then 'lower'
            when dept_avg < comp_avg then 'higher'
            else 'same' end comparison 
from calc

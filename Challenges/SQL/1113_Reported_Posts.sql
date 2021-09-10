with cte as(
    select action_date,
           action,
           extra,
           post_id
from actions
where action  = 'report' and extra is not null
)
select extra report_reason,
       count(distinct post_id) report_count
from cte
where action_date = '2019-07-04'
group by 1

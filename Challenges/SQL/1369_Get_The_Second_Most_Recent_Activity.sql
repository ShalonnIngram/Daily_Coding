with count as (
select *,
       count(activity) over (partition by username) act_count,
       dense_rank() over (partition by username order by startDate desc) act_rnk
from useractivity
)
select username,
       activity,
       startdate,
       enddate
from count
where act_count = 1 or act_rnk = 2

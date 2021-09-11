
with cte as (
select tweet_id, length(content) content_len
from tweets
group by 1
)
select tweet_id
from cte
where content_len > 15

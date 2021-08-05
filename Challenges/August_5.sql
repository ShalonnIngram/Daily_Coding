512. Game Play Analysis II
with cte as (
    select player_id, min(event_date), device_id
    from activity
    group by player_id
)
select player_id, device_id
from cte

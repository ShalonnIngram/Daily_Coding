
select user_id, count(follower_id) followers_count
from followers
group by 1

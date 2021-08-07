
1729. Find Followers Count
select user_id, count(follower_id) followers_count
from followers
group by 1


1683. Invalid Tweets
with cte as (
select tweet_id, length(content) content_len
from tweets
group by 1
)
select tweet_id
from cte
where content_len > 15


1587. Bank Account Summary II
with cte as (
select name, sum(amount) balance
from users u
join transactions t
on u.account = t.account
group by 1
)

select name, balance
from cte
where balance > 10000


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

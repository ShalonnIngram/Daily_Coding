with cte as (
    select num, count(num) sum
    from my_numbers
    group by 1
)
select max(num) num
from cte
where sum = 1

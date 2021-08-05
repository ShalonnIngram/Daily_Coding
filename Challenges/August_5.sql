512. Game Play Analysis II
with cte as (
    select player_id, min(event_date), device_id
    from activity
    group by player_id
)
select player_id, device_id
from cte



619. Biggest Single Number
with cte as (
    select num, count(num) sum
    from my_numbers
    group by 1
)
select max(num) num
from cte
where sum = 1


1068. Product Sales Analysis I
select product_name, 
       year,
       price
from sales s  
join product p
on s.product_id = p.product_id
group by sale_id


1069. Product Sales Analysis II
select product_id, sum(quantity) total_quantity
from sales s
group by 1

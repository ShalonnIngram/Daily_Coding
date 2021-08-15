1069. Product Sales Analysis II
select product_id, sum(quantity) total_quantity
from sales s
group by 1

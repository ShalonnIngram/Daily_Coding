select product_name,
       sum(unit) unit
from products p
left join orders o
on p.product_id = o.product_id
where month(order_date) = 2 
group by 1
having sum(unit) >= 100

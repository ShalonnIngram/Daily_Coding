select P.product_id,
round(sum(u.units*p.price)/sum(u.units),2) as average_price
from
Prices P, UnitsSold U
where P.product_id = U.product_id
and purchase_date between start_date and end_date
group by p.product_id
order by product_id

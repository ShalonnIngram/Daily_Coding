select name,
       sum(rest) rest,
       sum(paid) paid,
       sum(canceled) canceled,
       sum(refunded) refunded
from product p
join invoice i
on p.product_id = i.product_id
group by 1
order by 1

select name,
       ifnull(sum(rest),0) rest,
       ifnull(sum(paid),0) paid,
       ifnull(sum(canceled),0) canceled,
       ifnull(sum(refunded),0) refunded
from product p
left join invoice i
on p.product_id = i.product_id
group by 1
order by 1

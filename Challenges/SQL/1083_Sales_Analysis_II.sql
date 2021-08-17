1083. Sales Analysis II
select distinct buyer_id
from sales s
join product p
on s.product_id = p.product_id
where product_name = 'S8' and buyer_id not in
    (select buyer_id
    from sales s
    join product p
    on s.product_id = p.product_id
    where product_name = 'iPhone')

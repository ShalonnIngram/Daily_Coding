1890. The Latest Login in 2020
select user_id,
       max(time_stamp) last_stamp
from logins
where year(time_stamp) = '2020'
group by 1


1795. Rearrange Products Table
select product_id,
      'store1' store,
       store1 price
from products
where store1 is not null

union

select product_id,
      'store2' store,
       store2 price
from products
where store2 is not null

union

select product_id,
      'store3' store,
      store3 price
from products
where store3 is not null


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

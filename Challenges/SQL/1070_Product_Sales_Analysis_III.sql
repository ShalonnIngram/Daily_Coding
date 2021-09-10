with t1 as (
select s.product_id product_id,
       year,
       quantity,
       price,
       rank() over (partition by product_id order by year) rnk
from sales s
join product p
on s.product_id = p.product_id
)
select product_id,
       year first_year,
       quantity,
       price
from t1
where rnk = 1

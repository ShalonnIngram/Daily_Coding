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




1757. Recyclable and Low Fat Products
select product_id
from products p
where low_fats = 'Y' and recyclable = 'Y'



1069. Product Sales Analysis II
select product_id, sum(quantity) total_quantity
from sales
group by 1



1050. Actors and Directors Who Cooperated At Least Three Times
with cte as (
    select actor_id, count(actor_id) act_count, director_id, count(director_id) dir_count
    from actordirector
    group by 1
)
select actor_id, director_id
from cte
where act_count >= 3 and dir_count >= 3


OR 


with cte as (
    select *,
    rank() over (partition by actor_id, director_id order by timestamp) as rnk
    from actordirector
)
select actor_id, director_id
from cte
where rnk >= 3

OR

select actor_id, director_id
from actordirector
group by 1, 2
having count(*) >= 3




1076. Project Employees II
with cte as (
    select project_id, sum(employee_id) emp
    from project
    group by 1
)
select project_id 
from cte
having max(emp)



OR


select project_id
from (
    select project_id,
    rank() over(order by count(distinct employee_id) desc) as rnk
    from Project
    group by 1) a
where rnk = 1



1148. Article Views I
select distinct author_id as id
from views
where author_id = viewer_id
order by 1 asc


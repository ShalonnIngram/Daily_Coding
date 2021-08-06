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


1075. Project Employees I
select project_id, round(avg(experience_years), 2) average_years
from project p
join employee e
on p.employee_id = e.employee_id
group by 1



1741. Find Total Time Spent by Each Employee
select event_day day,
       emp_id,
       sum(out_time - in_time) total_time
from employees
group by 1, 2



607. Sales Person
select name 
from salesperson
where sales_id not in
    (select o.sales_id
    from company c
    join orders o
    on c.com_id = o.com_id
    where c.name = 'RED')


511. Game Play Analysis I
  select player_id, min(event_date) as first_login
  from activity
  group by player_id
  
  
512. Game Play Analysis II 
  select player_id, device_id
  from
    (select player_id, min(event_date), device_id
    from activity
    group by 1) sub


577. Employee Bonus
select e.name, b.bonus
from employee e
left join bonus b
on e.empid = b.empid
where b.bonus < 1000 or bonus is null


584. Find Customer Referee
select name
from customer
where referee_id != 2 or referee_id is null


586. Customer Placing the Largest Number of Orders
select customer_number
from
    (select max(customer_number) as customer_number
    from orders) sub


586. Customer Placing the Largest Number of Orders
select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1
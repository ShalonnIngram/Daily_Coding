586. Customer Placing the Largest Number of Orders
select customer_number
from
    (select max(customer_number) as customer_number
    from orders) sub

1479. Sales by Day of the Week
select item_category CATEGORY,
       sum(case when dayname(order_date) = 0 then quantity else 0 end) MONDAY,
       sum(case when dayname(order_date) = 1 then quantity else 0 end) TUESDAY,
       sum(case when dayname(order_date) = 2 then quantity else 0 end) WEDNESDAY,
       sum(case when dayname(order_date) = 3 then quantity else 0 end) THURSDAY,
       sum(case when dayname(order_date) = 4 then quantity else 0 end) FRIDAY,
       sum(case when dayname(order_date) = 5 then quantity else 0 end) SATURDAY,
       sum(case when dayname(order_date) = 6 then quantity else 0 end) SUNDAY
from items i
left join orders o
on o.item_id = i.item_id
group by 1
order by 1 asc

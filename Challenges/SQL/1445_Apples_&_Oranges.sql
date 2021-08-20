select a.sale_date SALE_DATE,
       (b.sold_num - a.sold_num) DIFF
from sales a
join sales b
on a.sale_date = b.sale_date
group by 1
       

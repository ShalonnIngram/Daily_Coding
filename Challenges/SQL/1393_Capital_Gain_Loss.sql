1393. Capital Gain/Loss
select stock_name,
       sum(case when operation = 'buy' then -price else price end) capital_gain_loss 
from stocks
group by 1

select round(avg(order_date = customer_pref_delivery_date) * 100, 2) immediate_percentage
from delivery

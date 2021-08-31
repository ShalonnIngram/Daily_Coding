select country_name,
       case 
       when avg(weather_state) <= 15 then "Cold"
       when avg(weather_state) >= 25 then "Hot" else "Warm" 
       end as weather_type
from countries c
join weather w
on c.country_id = w.country_id
where month(day) = 11
group by 1

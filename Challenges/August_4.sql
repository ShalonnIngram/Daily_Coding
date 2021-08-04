
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

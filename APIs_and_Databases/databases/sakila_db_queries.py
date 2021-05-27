
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice



import sqlalchemy
import pymysql
from pprint import pprint


engine = sqlalchemy.create_engine("mysql+pymysql://root:trublue6@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)


# 1. Select all the actors with the first name of your choice
query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'PENELOPE')
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)


# 2. Select all the actors and the films they have been in
join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)


# 3. Select all the actors that have appeared in a category of a comedy of your choice
# 4. Select all the comedic films and sort them by rental rate
# 5. Using one of the statements above, add a GROUP BY statement of your choice
# 6. Using one of the statements above, add a ORDER BY statement of your choice

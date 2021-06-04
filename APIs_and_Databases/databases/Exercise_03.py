
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

engine = sqlalchemy.create_engine("mysql+pymysql://root:localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)


query = sqlalchemy.update(films).values(rental_duration=10).where(film.columns.length > 150)

import sqlalchemy                                                                                                                                                 
import pymysql                                                                                                                                                    
from pprint import pprint                                                                                                                                         
                                                                                                                                                                  
engine = sqlalchemy.create_engine("mysql+pymysql://root:trublue6@localhost/sakila")                                                                               
connection = engine.connect()                                                                                                                                     
metadata = sqlalchemy.MetaData()                                                                                                                                  
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)                                                                                  
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)                                                                                    
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)                                                                        
                                                                                                                                                                  
# returns columns in the sakila.actor table along with its metadata                                                                                               
# print(actor.columns.keys())                                                                                                                                     
# print(repr(metadata.tables['actor']))                                                                                                                           
                                                                                                                                                                  
                                                                                                                                                                  
# SELECT * FROM actor                                                                                                                                             
 query = sqlalchemy.select(actor)                                                                                                                                 
result_proxy = connection.execute(query)                                                                                                                          
                                                                                                                                                                  
for result in result_proxy:                                                                                                                                       
    print(f"first name: {result['first_name']}")                                                                                                                  
                                                                                                                                                                  
# to fetch all columns                                                                                                                                            
all_columns = result_proxy.fetchall() # or fetchone()                                                                                                             
# access columns from the result                                                                                                                                  
all_columns = result_proxy.fetchone()                                                                                                                             
print(all_columns["first_name"])                                                                                                                                  
print(result.keys())                                                                                                                                              
                                                                                                                                                                  
                                                                                                                                                                  
                                                                                                                                                                  
# to fetch 5 columns in the sakila.actor table                                                                                                                    
result_set = result_proxy.fetchmany(5)                                                                                                                            
                                                                                                                                                                  
# using the WHERE clause to filter data from the sakila.actor table                                                                                               
# SELECT * FROM sakila.actor WHERE first_name = "JENNIFER"                                                                                                        
query2 = sqlalchemy.select([actor]).where(actor.columns.first_name == "Jennifer")                                                                                 
                                                                                                                                                                  
# using the IN statement to filter data in the sakila.actor table                                                                                                 
# SELECT * FROM sakila.actor WHERE first_name IN ("PENELOPE", "JOHN", "UMA")                                                                                      
query = sqlalchemy.select([actor]).where(actor.columns.first_name.in_(["PENELOPE", "JOHN", "UMA"]))                                                               
                                                                                                                                                                  
# using AND, OR, NOT to filter data in the sakila.actor table                                                                                                     
SELECT * FROM sakila.film WHERE length > 60 AND rating = "PG";                                                                                                    
query = sqlalchemy.select([film]).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating == "PG"))                                                   
query = sqlalchemy.select([film]).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating != "PG"))                                                   
                                                                                                                                                                  
                                                                                                                                                                  
# using the ORDER BY statement                                                                                                                                    
SELECT * FROM sakila.film ORDER BY replacement_cost ASC;                                                                                                          
query = sqlalchemy.select([film]).order_by(sqlalchemy.asc(film.columns.replacement_cost))                                                                         
                                                                                                                                                                  
# SUM & other functions                                                                                                                                           
SELECT SUM(length) FROM sakila.film;                                                                                                                              
query = sqlalchemy.select([sqlalchemy.func.sum(film.columns.length)])                                                                                             
                                                                                                                                                                  
                                                                                                                                                                  
# JOINS                                                                                                                                                           
join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)     
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)               
result_proxy = connection.execute(query)                                                                                                                          
result_set = result_proxy.fetchall()                                                                                                                              
                                                                                                                                                                  
# create a new table                                                                                                                                              
newTable = sqlalchemy.Table('newTable', metadata,                                                                                                                 
                       sqlalchemy.Column('Id', sqlalchemy.Integer()),                                                                                             
                       sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),                                                                         
                       sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),                                                                            
                       sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)                                                                            
              )                                                                                                                                                   
                                                                                                                                                                  
metadata.create_all(engine)                                                                                                                                       
                                                                                                                                                                  
                                                                                                                                                                  
# INSERT statement                                                                                                                                                
newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)                                                                            
                                                                                                                                                                  
query = sqlalchemy.insert(newTable).values(Id=1, name='Software Ninjaneer', salary=60000.00, active=True)                                                         
result_proxy = connection.execute(query)                                                                                                                          
                                                                                                                                                                  
# INSERT multiple rows at once                                                                                                                                    
query = sqlalchemy.insert(newTable)                                                                                                                               
new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},                                                                                      
               {'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]                                                                                       
result_proxy = connection.execute(query,new_records)                                                                                                              
                                                                                                                                                                  
                                                                                                                                                                  
# UPDATE  statement                                                                                                                                               
import sqlalchemy                                                                                                                                                 
engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')                                                                           
connection = engine.connect()                                                                                                                                     
metadata = sqlalchemy.MetaData()                                                                                                                                  
newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)                                                                            
query = sqlalchemy.update(newTable).values(salary=100000).where(newTable.columns.Id == 1)                                                                         
result = connection.execute(query)                                                                                                                                
                                                                                                                                                                  
# DELETE statement                                                                                                                                                
import sqlalchemy                                                                                                                                                 
engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')                                                                           
connection = engine.connect()                                                                                                                                     
metadata = sqlalchemy.MetaData()                                                                                                                                  
newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)                                                                            
query = sqlalchemy.delete(newTable).where(newTable.columns.salary < 100000)                                                                                       
results = connection.execute(query)                                                                                                                               

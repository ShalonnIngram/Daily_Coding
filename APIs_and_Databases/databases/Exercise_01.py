

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.


import sqlalchemy                                                                            
import pymysql                                                                               
from pprint import pprint                                                                    
                                                                                             
engine = sqlalchemy.create_engine("mysql+pymysql://root:trublue6@localhost/sakila")          
connection = engine.connect()                                                                
metadata = sqlalchemy.MetaData()                                                             
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)               
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)       
                                                                                             
pprint(film)                                                                                 
pprint(category)                                                                             
                                                                                             

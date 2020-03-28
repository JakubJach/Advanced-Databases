Jakub Jachowicz

LAB 2 - Introduction to SQLAlchemy

Exercise 1:


```python
from sqlalchemy import create_engine, MetaData, Table, select

db_string = "postgres://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"
db = create_engine(db_string)

print(db.table_names())

metadata = MetaData()
```

    ['staff', 'category', 'film_category', 'country', 'actor', 'language', 'store', 'rental', 'city', 'address', 'film_actor', 'payment', 'users', 'film', 'customer', 'inventory']
    

Exercise 2:

i. information_schema indicates that each staff member entry in 'staff' table has address_id which corresponds to specific entry in 'address' table; then, each address has city_id that corresponds to city_id in 'city' table, and then  each city has country_id corresponding to country_id in 'country' table

To explore relationship between tables, it is necessary to find address through address_id, then city through city_id and, finally, country by country_id.

ii. each film in 'film' table has language_id, which corresponds to language_id of that language in 'language' table; as for actors and films, each actor in 'actor' table has an actor_id corresponding to actor_id in table 'film_actor' in this table each actor_id is connected to film_id, that corresponds to film_id column in 'film' table

To explore relationship between these tables, it is necessary to find actor's movies using his actor_id, to get a list of his appearances. Then, through film_id, identify movies, and use language_id to check languages.

Exercise 3:


```python
category_table = Table("category", metadata, autoload = True, autoload_with = db)

stmt = select([category_table.c.name])
results = db.execute(stmt).fetchall()

print('\nIn total there are %d movie categories' % len(results))
```

    
    In total there are 16 movie categories
    

Exercise 4:


```python
limit = 2

for index, row in zip(range(limit),results):
    print(row.name)

#for row in results:
#    print(row.name)
#    if(row == 2): break
#print(type(results))
```

    Action
    Animation
    

Exercise 5:


```python
film_table = Table("film", metadata, autoload = True, autoload_with = db)

stmt = select([film_table.c.release_year]).group_by(film_table.c.release_year)
results = db.execute(stmt)

for row in results:
    print(row.release_year)
```

    2006
    

It appears, that all movies are from 2006, and we do not have any information about days or months of premiere, so there is no youngest or oldest movie - all of them are the same age :D.

Exercise 6:


```python
actor_table = Table("actor", metadata, autoload = True, autoload_with = db)

stmt = select([actor_table.c.actor_id,actor_table.c.first_name,actor_table.c.last_name])
stmt = stmt.where(actor_table.c.first_name == 'Olympia')
results = db.execute(stmt)

for row in results:
    print(row)
```

    (171, 'Olympia', 'Pfeiffer')
    


```python
stmt = select([actor_table.c.actor_id,actor_table.c.first_name,actor_table.c.last_name])
stmt = stmt.where(actor_table.c.first_name == 'Julia')
results = db.execute(stmt)

for row in results:
    print(row)
```

    (27, 'Julia', 'Mcqueen')
    (47, 'Julia', 'Barrymore')
    (186, 'Julia', 'Zellweger')
    (199, 'Julia', 'Fawcett')
    


```python
stmt = select([actor_table.c.actor_id,actor_table.c.first_name,actor_table.c.last_name])
stmt = stmt.where(actor_table.c.first_name == 'Ellen')
results = db.execute(stmt)

for row in results:
    print(row)
    
results.close()
```

    (93, 'Ellen', 'Presley')
    

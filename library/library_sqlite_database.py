import sqlite3
import json
from pathlib import Path


# movies = json.loads(Path("movies.json").read_text())
# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
  # command = "INSERT INTO Movies VALUES(?, ?, ?)"
  command = "SELECT * FROM Movies"
  # for movie in movies:
  #   conn.execute(command, tuple(movie.values()))
  cursor = conn.execute(command)
  # for row in cursor:
  #   print(row)
  movies = cursor.fetchall()
  print(movies)
  # conn.commit()



''' Working with SQLite in python:
Here we will store data in SQLite database. SQLite is a very lightweight database we use to store data
in an aplication. This is the technilogy we use in small applications. It allows us to easily sotre and 
format data like a table of rows and columns. 

1. Let's start with importing sqlite3 module on the top.
2. We have a json file movies.json in the current dirctory. Let's read the file and store 
   the data on the sqlite database.
3. So we alos need json module so import json also Path class.  
4. Now create a path object for the json file and read_text() method to read
5. Then pass all these to json.loads() this returns a list of movies. 
6. Then let's print and see things are working or not so far. It returns a list of dictionary: 
   [{'id': 1, 'name': 'Terminator', 'Year': '1989'}, {'id': 2, 'name': 'Predator', 'Year': '1987'}]
7. Now let's store this list in a database:
8. Now the sqlite object has method called connect() we pass argument here, the name of our database file
   let's call it db.sqlite3 it could be any name. If this file does not exists it will create for us. 
9. It return a connection object the connection object should be closed when we are done with it. So better
   to use with statement instead close()
10 Next we need to create command. This command is basically the instruction to the database, like we are 
   obtaining data, creating data, deleting data etc. So creating a commad;
11. command = "INSERT INTO Movies VALUES(?, ?, ?)" set to stirng. We are assuming we have a table called movies 
    where we store moveis. The we add VALUES(?, ?, ?) these question marks are the placeholder for the values 
    that we provide in next step. So we have the table of movies has 3 columns id, name, year.
12. Next we need to iterate over the movies list. like for movie in movies: then we need to execute the command.
13. Use the conn object it has a method called .execute() and pass the commad as first argument and the second
    argument is the actual values. So each movie object in the for loop is a dictionary that has key:value.
14. So we can call movie.values() and we need to get the value and put them into a tuple.
15. After this is done lastly we need to commit the connection: conn.commit() at this point all the changes
    will be written into the database. 
16. Now if we run this program this will return an error. 
    OutPut: sqlite3.OperationalError: no such table: Movies 
    becasue we are working with an empty database and it has no table.
17. We need to crete a movies table first in the sqlite3. If we go to google and search for 
    'db browser for sqlite' then open this site "https://sqlitebrowser.org/" then on this page
    https://sqlitebrowser.org/dl/ donwnload your executable dmg file and install the correct db browser.
18. When we open as new user we will see the this is empty so we will do below step to create new table;
    a. On the top Open Database
    b. Let's open the database file in this case, db.sqlite3 from my computer
    c. we can see the file open in DB browser but there is no table(0). Let's create one
    d. Give the name of the table on the top
    e. Then we need to add 3 columns as click on Add Field button. It appears the option to add fields
    f. Give name of the field and choose the type of the field.
    g. Our first column is id and it is integer. Then we choose it as primary key(PK), which means we 
       are specifing id is the unique indentfier for each movies. or we can say each movies should have 
       unique id.
    h. Let's anothe field called Name and type is Text
    i. And finally, another field Year and type is integer. Then save the changes and go back to the home
       and can see 1 table(Movies) is added and there are 3 fileds for the columns.
    j. Note: in the add field options we can see a NN checkbox if we mark it that means we are telling sqlite
       that data on this column can not be Null. In other words, we can not have a movie with out Name or year.
    k. Now run the program once again. and this time it should not give error. 
    l. No go back to DB Browser and this time we can see the movie data on Browse Data tab. 
19. Now we have a database and we can also read the movies data from the databse.
20. To do so we do not need json file since we are going to read from database so comment out line-6
21. We need to connect database so we need line 9.
22. we need to change the command. instead insert we need to select all the movies. So comment out line 9
23. And write new line of code command = "SELECT * FROM Movies" and we do not need iterate.
24. We just need to execute this command. con.execute(command) pass the argument command. And this will return
    a cursor, when we read data froma databse it retunrs a cursor, a cursoe is a iterable object. 
25. So we can iterate over the cursor a row at a time, so this will be for row in cursor: simplily print(row)
26. And we do not need conn.commit() to read from database. it needs when you write in database. So comment out
27. Then run the program and we get a tuple for each iteration. 
    OutPut: 
    (1, 'Terminator', 1989)
    (2, 'Predator', 1987)
28. we also get a list of tuples by using another method called fetchall() in this case we do not need 
    to iterate. so comment out for loop codes. OutPut: [(1, 'Terminator', 1989), (2, 'Predator', 1987)] '''

import json
from pathlib import Path


# movies = [
#   {"id": 1, "name": "Terminator", "Year": "1989"},
#   {"id": 2, "name": "Predator", "Year": "1987"}
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[1]["name"])

''' Working with JSON in python:
JSON stands for javascript object notation. And it is a popular way to format data
in human readable way. Most the websites arovide data in JSON format. 

Let's start wrok with json;

1. On the to we import json module
2. Now create a array movies = [] each object in the array is a dictionary. Each dictionay has key: value 
3. Now in json object use dumps() method and supply movies as parameter to format the movies data as JSON
4. Then store in data variable. and print(data)
5. And we get the OutPut in terminal: 
   [{"id": 1, "name": "Terminator", "Year": "1989"}, {"id": 2, "name": "Predator", "Year": "1987"}]
6. Note: the output is identical as we difine the movies array. But we can create JSON file and write
7. To do so import Path class from pathlib module
8. Then instead print line-11, create a Path("movies.json") object which create a json file in current directory
9. Then call .write_text() method and pass data as parameter this function write the data in json format
   in the movies.json file. 
10. Now run the program. It creates the movies.json file in the currernt directory with the data in json format
11. So this is how to write in json file.
12. Let's imagine we got the movies.json file from somewhere else like from facebook, twitter etc
    so we should able to read the data.
13. So we do not need the data creation and dumps() so commmented out all lines: 5-12
14. And create the Path("movies.json") object and call the read_text() method
15. Store this to let's say data varialbe. Now the data is string and formated as json
16. Next we need to parse this string into a array of object. So we call loads() method 
    and pass data as parameter and store it to a variable(let's say movies)
17. Then print movies and get the OutPut: an array of dictionaries. 
    [{'id': 1, 'name': 'Terminator', 'Year': '1989'}, {'id': 2, 'name': 'Predator', 'Year': '1987'}] 
18. And we can get info by filtering like, we can get any item using [0], name ["name"] etc. '''

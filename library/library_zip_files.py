from pathlib import Path
from zipfile import ZipFile


''' Working with zip files in python: 
So from from zipfile module import Zipfile class '''

# Now we can create a zipfile object, let's call the file files.zip
# And the 2nd argument is w short from of write
# So this statement will write in zip file in current folder

# zipFile = ZipFile("files.zip", "w")

''' Now let's say we will get all the files from Types directory and write them to the zip file. 
It is very easy;

1. We create a Path() object and referrence to Types directory; Path("Types")
2. Then call .rglob() method to recursively find all the files "*.*" as we know it return generator
3. So we iterate over it for path in Path()
4. Then close() the method line 24. '''

# for path in Path("Types").rglob("*.*"):
#   zip.write(path)
# zip.close()

''' Bit if something goes wrong the zip.close() method may not called. So better use try block or with
statement, which is more cleaner. so final code looks like below; 
And if you run the program the zip file will create in the current directory '''

with ZipFile("files.zip", "w") as zip:
  for path in Path("Types").rglob("*.*"):
    zip.write(path)


''' Now let's go ahead and read it's content: '''
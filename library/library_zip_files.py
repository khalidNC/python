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

# with ZipFile("files.zip", "w") as zip:
#   for path in Path("Types").rglob("*.*"):
#     zip.write(path)


''' Now let's go ahead and read it's content: 
1. First comment the codes line 30-32
2. write ZipFile("files.zip") object and this time we just read so no 2nd argument and inside with statement
3. Then call a method, namelist() which returns all the files in zip file
4. Let's print now'''

with ZipFile("files.zip") as zip:
  print(zip.namelist())
  print(zip.getinfo("Types/number.py")) # Output: <ZipInfo filename='Types/number.py' filemode='-rw-r--r--' file_size=1734>
  info = zip.getinfo("Types/number.py") # We can also print info object
  print(info.filename)
  print(info.file_size)
  print(info.compress_size)
  print(info.date_time)
  # Now we can also extract the zip to another location.
  # This will create "extract" directory in the current directory and extract the zip file there
  zip.extractall("extract")


''' Line-42:
 OutPut: ['Types/number.py', 'Types/variable.py', 'Types/strings.py']
These are the list of all files inside the zip file. We can get information of any of these files.

line-43:
For examples, we copy "Types/number.py" and pass as argument in this method; .getinfo() '''

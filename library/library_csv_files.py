import csv


''' Working with CSV Files in Python:
CSV (Comma-Separated Values) files are a common way to store tabular data. 
Python provides the csv module to work with CSV files. Here is an example 
and break down the steps for reading and writing CSV files. '''

''' Writing CSV Files:
Now, let's look at how to write data to a CSV file: 
On the top import csv 
Open the file to use a buit-in function open(). It takes 2 arguments, file and mode('w' 'r') '''

# file = open("data.csv", "w")
# This retruns a file object. And open scv file in write mode and a new csv file created in current directory
# Then make sure to close() it
# file.close()
# But the better approach to use with statement. So the code will be;
# csv.writer(csv_file): the csv module has a method writer() to create file that takes file_name as parameter
# Then writer.writerow([]): here we pass data(list) as heading of the file. Then add other rows in same way
''' Now run the program. And I can see a csv file(data.csv) is created in the current directory. 
OutPut: 
Name,Age,City
Borna,35,Khulna
Nameera,8,Dhaka

This is like simplified spreadsheet. we have table of data each line represents a row and every cells is
separated by a comma. This is a very simple way to store data. '''

# with open("data.csv", "w") as csv_file:
#   writer = csv.writer(csv_file)
#   writer.writerow(["Name", "Age", "City"])
#   writer.writerow(["Borna", "35", "Khulna"])
#   writer.writerow(["Nameera", "8", "Dhaka"])


''' Reading csv file: 
Let's say we have the data.csv file and we need to read from the file: 
So the code will be:
Use open() method and this time no mode w/r in with statement.
Then instead writer use method reader()
Now we can call the list() function to get all the data from the csv file and converted to a list object.
Let's print and take a look. '''

with open("data.csv") as csv_file:
  reader = csv.reader(csv_file)
  # print(list(reader))
  for row in reader:
    print(row)

# OutPut: [['Name', 'Age', 'City'], ['Borna', '35', 'Khulna'], ['Nameera', '8', 'Dhaka']]
# We get a list of list. Each line of the csv file is a list of object. 
# Note: all are string even it's a number
# We can also iterate over the objet line 48 and comment out line 47
# Now we have 3 row and each row is arry of string
''' OutPut:
['Name', 'Age', 'City']
['Borna', '35', 'Khulna']
['Nameera', '8', 'Dhaka'] '''

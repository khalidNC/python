from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
import getpass
from string import Template


# Create Template object, pass template file as string also call .read_text() method
template = Template(Path("template.html").read_text())

# Creating MIMEMultipart object
message = MIMEMultipart()

# Set differe headers to the message object
message["from"] = "Md Khalid Hussain"
message["to"] = "khalidpython3@gmail.com"
message["subject"] = "This is a computer generated test email"

# Call substitute() method to relapce $parameter in template file. It takes dictionary key:value
# We can also pass key=argument like name_of_user="Khalid"
body = template.substitute({"name_of_user": "Khalid"})

# Create MIMEText() object and supply text
message.attach(MIMEText(body, "html"))
# Create MIMEImage() object and it takes path object and convert to binary
message.attach(MIMEImage(Path("khalid.png").read_bytes()))

# Get email password from user as input using getpass() method
passwrod = getpass.getpass("Enter Your Password Here: ")

# Create smtp() object with arguments host=, and port. We need to close the server but better use with
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
  # Connect with smtp server saying "hello" to the server
  smpt.ehlo()
  # Start with tls(transprot layer security) it encryptes all data in smpt server
  smpt.starttls()
  # Login to sender email. get email passwaord from user as inoput. 
  smpt.login("khalidpython3@gmail.com", passwrod)
  # Sending message: use send_message() method and supply message object
  smpt.send_message(message)
  print("Email sent....")

''' Here we are sending email with plain text as email body. But email body have many lines of codes
and we do not want write those here in mesage[body] object. Quite often we put that contect in a separate
file as template and we use html to build that template
So We create a new file in current directory called template.html then go to the file and type(!) and
hit tab button that will generate some html codes quickly. Now we have a basic html template as below:

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>

For sending email;
1. we do not need <head> so we delete this section in template.html file. 

2. And inside <body> we will write the email content. Here is an example of content:
   Dear user, This is a test purpose email.
   a. here, if we want to dynamicly replace the name of the user then let's use a parameter that we replace
      later. To define a parameter start with a doller sign and give the parameter name. so it will be like,

   b. Dear $name_of_user, This is a test purpose email. So we do this changes on the template.html file

3. Now we will import template class from string module. We will use the Template class to replace $name
   on the template. To do this;

4. Let's create Template() object then need to pass the template as string. So here we create Path()
   and load "template_file.html". We will also call .read_text() method this will return entire 
   content on template file as string.

5. Now we will store this in a variable defined as template. And we have a template object now. 
   This template object has a method called .substitue() with this method we can replace the parameter
   in tmplate.html file dynamicly.

6. So in message object secction where we attach body we call the substitute() method and sotre in a 
variable let's define as body. The method take argument as dictionary{} with key:value or keyword=argument.

7. Now pass this body to MIMEText() method as fisrt argument, and "html" as second argument.

8. Now run the program and see the email is sent with html content. 

Note: This template does not use any featurs of html format so this template returns a plain text with
all lines together there is no line gap or anything. So we need to use html features to make the email 
improved. '''

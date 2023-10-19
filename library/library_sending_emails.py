from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import getpass
import smtplib


# Creating MIMEMultipart object
message = MIMEMultipart()
# Set different headers related emails supported by MIMEMultipart object
message["from"] = "Md Khalid Hussain"
message["to"] = "khalid280284@gmail.com"
message["subject"] = "This is a test purpose email."
message.attach(MIMEText("body"))
message.attach(MIMEImage(Path("khalid.png").read_bytes()))

# Create getpass() object
password = getpass.getpass("Enter Your Password: ")


# Creating smtp object. Supply 2 keyword-arguments host=, port= and this returns a smpt object
# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# When we done with it make sure to close this to release this resource
# smtp.close()
# Prefer to use with statement instead the abvoe. So comment out above codes and write below with

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  # Provide password as plain text, this is basic not do not use in real program
  # smtp.login("khalidpython3@gmail.com", "*******")

  # Get password from the user as input:
  smtp.login("khalidpython3@gmail.com", password)
  smtp.send_message(message)
  print("Email has been sent...")


''' Sending emails in python:
This is very usefull in a situation when you have a set of customers and you want to send 
various eamils based on their interest. 

Sending emails in Python can be achieved using the smtplib library, which allows you to 
send email messages through Simple Mail Transfer Protocol (SMTP) servers. In addition to 
smtplib, you'll also need the email library to create and format email messages. 

Basically we need to import a couple of module and classes to create email message and 
to connect to smtp server fro sending emails. Let's start:;

1. Import:
    from email.mime.multopart import MIMEMultipart
      Meaning: in email package in python standard library we have a subpackage mime(Multipurpose Internet
      Mail Extension) in this packages we have another subpackage called multipart which has class called
      MIMEMultipart. With this object we can send an email message that include both html and plain text 
      content. 
        
2. Creating MIMEMultipart object:
     a. Create MIMEMultipart() and store it in message variable. 
     b. We set various headers that supported by MIMEMultipart object for email like "From", "To", "Subject"  
     c. But it does not have header for "body". So to set the body we need to attach the body to message.
        The message object has method .attach() we will call it now.
     d. attach() method takes payload as argument. A payload can be text, image, or other type that supports
        mime protocol. 

3. Import: 
    from email.mime.text import MIMEText

4. Now we can call MIMEText() to create the body of the message and pass it to .attach() method.

5. Then the MIMEText() method takes 2 arguments; one is text e.g "body", Another could be "plain" text
   and this is deafult you can avoid the second argument.
   Note: if you pass html content as first argument then the second argument will be "html".

6. Now we have a email message object and we need to send them using the smtp server.

7. To do so import smtplib module. This module has class called SMTP

8. SMTP() method takes 2 keyword=arguments, 1st one is, host="smtp.gmail.com" 2nd one is, port=587

9. Now write this with 'with' statement and we have to do a couple of things before sending email
    a. First we need to connect with smtp server: so we called smtp.ehlo() method to connect. This method
       is a part of smtp protocol when sending emial. This is bassically telling smtp server "Hey I am a 
       client and I want to send an email. So the communication between client and smtp server should start
       the (ehlo)hello message.
    b. Next we need to call smtp.starttls() method. And this method put smtp connection in tls mode. TLS mean
       Transport Layer Security. All the command we will send to smtp server will be encrypted.

10. Now we are ready to login to my email:
    a. So we call smtp.login() method, we pass our email and password here.
    b. But the login may not happen. It may raise authencation error: "raise SMTPAuthenticationError(code, resp)
       smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  
       https://support.google.com/mail/?p=BadCredentials g22-20020a1709029f9600b001c9e53b721csm3542074plq.261 - 
       gsmtp')"
    c. To solve this, we need to generate a app password on goolge account under security. Then use that app
       password in the login() method. In this page https://myaccount.google.com/apppasswords we can generate 
       the app password.
    d. In real project it must not provide plain text password. There are many ways to encrypt password we
       should follow one. 

11. Finally, we called smtp.send_message() method to send email. Here we pass the message object.

12. Now to confirmation print("Email has been sent...") in the terminal.

13. Run the program: Now save the changes and run the program and you can see the success message in your 
    terminal. and in your email inbox you receive the email. 
    
14. Note: in real project work there might have many errors so we need handle exception.

15. Attach image in the message:
      a. Now we will try to attach an image in the email message. So we need to import MIMEImage class.
      b. Then we keep an image in my current directory. 
      c. Then we call message.attach(MIMEImage()) and create MIMEImage() object and here we need to pass image 
         data in binary. 
      d. So we need to import Path class.
      e. Then will create a Path("file_path") object and pass in MIMEImage() method 
      f. Finally, we need to use .read_bytes() method this returns all the data in the file in binary.
16. Now run the program once again and we can see the success message and the email I received with image. '''


''' One important fact: In the real production code we can not privide plain text password. There are many ways
    to handle this. Here we will just take the password as input from the user, the owner of this script. 
    
    To do so we will use getpass() method. So,
    1. We will import getpass module
    2. Then create a getpass object and store in a variable called password. 
    3. Then pass this password object as 2nd arument in smtp.login() method. 
    4. The run the program and you will get "Enter Your Password: " option in your terminal. So enter
       the password and hit enter button. 
    5. So you will get the success message and you received the email. '''


import webbrowser


print("Deployment completed")
webbrowser.open("http://www.google.com")


''' Opening a web browser in python script:
Open browser spicially needs when you done with branch of task then you want to open those
in a browser. For example, you built a script to deploy to the production. You worked on your
local machine then run the script then it deploys to the webserver. Then you want to open this
in a browser. This is manual, but you can make it automated that the script will open the 
browser and go to the website after the deployment is done. 

So let's print("Deployment completed")
To open a browser we need to import webrowser module on the top
This module has method called open()
Here we need to simplily pass web address let's say "http://www.google.com" 
Now run the program and we will see the print message in the terminal and the the google site 
opens in a browser automatically. '''

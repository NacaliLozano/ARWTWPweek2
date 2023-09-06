#The script should now follow the structure:

#List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.

#Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
#You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.

#Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.

#Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.

#Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.


#!/usr/bin/env python3
import os
import requests
os.chdir("/data/feedback")
for file in os.listdir():
    try:
        with open(file) as f:
            lines = f.readlines()
            dictionary = {}
            dictionary["title"] = str(lines[0]).strip()
            dictionary["name"] = str(lines[1]).strip()
            dictionary["date"] = str(lines[2]).strip()
            dictionary["feedback"] = str(lines[3:]).strip()
            response = requests.post("http://35.225.226.209/feedback/", json=dictionary)
            print(response.status_code)
            print(response.request.body)
    except OSError:
        print("Error opening {}.".format(file))
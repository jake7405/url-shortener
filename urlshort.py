#!/usr/bin/env python3
import requests
import getpass

###
# https://dev.bitly.com/api-reference
###

print("Bitly Shortener v1.0")
print("By Jacob Blackstone\n")
print("Input your credentials below.\n")

# user input account credentials
username = input("Enter username: ")
password = getpass.getpass("Enter Password: ")

# obtain access token
auth = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth.status_code == 200:
    # response 200 is a good request
    access_token = auth.content.decode()    # decode access token
    print("SUCCESS: access token received")
else:
    # response if 200 not received/bad credentials/failed connection
    print("Authorization Failed! Try again.")
    exit()

# constructing request headers -- use token to auth
headers = {"Authorization": f"Bearer {access_token}"}

# get account group UID
group = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if group.status_code == 200:
    # good response retreives the guid
    group_data = group.json()['groups'][0] # encode dictionary into JSON
    guid = group_data['guid']
else:
    print("Could not retreive GUID! Try again.")
    exit()

# shorten user-inputted URL
url = input("Enter URL you wish to shorten: ") # TODO append https:// if not present
short_resp = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
# new POST request to service that shortens links, same function as bit.ly
# we pass the GUID and URL collected above to POST
if short_resp.status_code == 200 or short_resp.status_code == 201:   # same idea as above, 200 = good request
    bitly_link = short_resp.json().get("link") 
    # get shortened link from JSON
    print("Shortened URL: ", bitly_link)
else: 
    print("Shortening failed. Try again.")
    exit()
    


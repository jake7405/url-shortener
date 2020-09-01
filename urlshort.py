#!/usr/bin/env python3
import requests
import getpass

print("Bitly Shortener v1.0")
print("By Jacob Blackstone\n")
print("Input your credentials below. Credential verification is in progress. Right now, it will just crash the program.\n")

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
    print("[!] Could not get access token. Try again.")
    exit()

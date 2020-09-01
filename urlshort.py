#!/usr/bin/env python3
import requests
import getpass

print("Bitly Shortener v1.0")
print("By Jacob Blackstone\n")
print("Input your credentials below. Credential verification is in progress. Right now, it will just crash the program.\n")

# user input account credentials
username = input("Enter username: ")
password = getpass.getpass("Enter Password: ")
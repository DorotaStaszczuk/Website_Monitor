import requests
from bs4 import BeautifulSoup
from datetime import datetime


# opening, reading and printing the file
c = open("config.txt", "r")
print("Config file content:")
for x in c:
    print(x)
c.close()

# If I put period always on the first line of a file, word to look for on a site
# on a second and url on the third I can download them using the method below
c = open("config.txt", "r")
period = c.readline()
look_for = c.readline()
url = c.readline()
print("Requirements downloaded")
c.close()

# checking if data was downloaded accordinly
print("Period: " + period)
print("Look_for: " + look_for)
print("url: " + url)

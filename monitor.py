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

# downloading the page
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=5)
print(r)

# getting status code
s = r.status_code()
print("Status code: " + s)

if s != 200:
    print("Website is down")
else:
    print("OK")

# checking if the download happened without any issues
r.raise_for_status()
print("Website downloaded: " + url)

# checking for response time
time = str(r.elapsed.total_seconds())

# parsing using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# looking for a word from config file
soup.find_all(look_for)

# if the word was not found
if soup.find_all(look_for) == None:
    print("Word not found")
    # wait number of seconds given in period
    time.sleep(period)
    continue

# if the word was found
else:
    print("Success")

# current date and time
date = str(datetime.now())

# opening logfile, saveing url, current date and time, status and reaction
# time of each site
l = open("logfile.txt", "a")
add = url + " " + date + " " + status + " " + time + " "

l.write(add)
l.close()
print("Results saved: ")

# checking what was saved
l = open("logfile.txt", "r")
print(l.readlines())
l.close()

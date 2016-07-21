import urllib.request
from BeautifulSoup import *

url = input("Enter URL:")

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup("a")

for tag in tags:
    print(tag.get("href", None))
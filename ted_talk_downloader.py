import requests
from bs4 import BeautifulSoup
import sys
import re

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("ERROR PLEASE ENTER TED TALK URL")

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="html")

for val in soup.find_all("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)
print(result)
result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
mp4_url = result_mp4.split('"')[0]

print("Downloading video from ", mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in....", file_name)

r=requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

print("Process finished")

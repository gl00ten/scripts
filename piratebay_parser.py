from bs4 import BeautifulSoup
import requests,re, subprocess

searchString = "public domain" # change this before running
torrentClientBinLocation = "/usr/bin/transmission-gtk"

# go to gui options and disable show torrent options dialog


for i in range(1,100):
    try:
        result = requests.get("https://thepiratebay.rocks/search/" + searchString + "/" + str(i) + "/99/0")
        c = result.content
        soup = BeautifulSoup(c, 'html.parser')

        magnets = soup.find_all(href=re.compile("magnet"))

        for l in magnets:
          l1 = l.attrs.get("href")
          subprocess.run([torrentClientBinLocation,l1])

    except:
        pass
        
    

    

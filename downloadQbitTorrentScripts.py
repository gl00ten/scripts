# run with: python3 downloadQbitTorrentScripts.py | xargs wget
# then in qbitorrent you can go view -> search engine --> search plugins -> install a new one ->
# and select the good ones this got


import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins")
c = r.content
soup = BeautifulSoup(c, 'html.parser')

python_scripts = soup.find_all(href=re.compile("\.py$"))

for l in python_scripts:
    print(l.attrs.get("href"))


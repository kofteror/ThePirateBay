from pyquery import PyQuery as pq
from lxml import etree
import urllib2
website="https://thepiratebay.org/search/"
append="/0/99/0"
i=0
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}


name=str(raw_input("enter serias name\n"))
name=name.split(" ")
print name
season=(raw_input("season number?\n"))
episode=(raw_input("enter number of episodes\n"))
season=str(str(season).zfill(2))
name.append("S"+season+"E"+episode.zfill(2))
for i in range(1,int(episode)+1):
    name[-1]="S"+season+"E"+str(i).zfill(2)
    middle="%20".join(name)
    request=urllib2.Request(website+middle+append,headers=hdr)
    response = urllib2.urlopen(request)
    html = response.read()
    parser=pq(html)
    tag=parser("td a")
    print tag
    flag =0
    for t in tag:
        if (flag):
            print t.get("href")
            break
        if (t.get("class")=="detLink" and not ("720p" in t.get("href"))):
            flag=1
   # print t.get("href")

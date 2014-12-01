import urlparse
import urllib
from bs4 import BeautifulSoup
from crawlerapp.models import Website

url = 'http://www.webcrawler.com/search/web?qsi=%s1&q=onlinedatingsites&aid=2aecfd91-196c-4811-a88a-f0fd033abf7b&ridx=3&fcoid=4&fcop=results-bottom&fpid=2'

num = 1

while num < 20:
    try:
        nextpage = url % num
        num += 1
        htmltext = urllib.urlopen(nextpage).read()
    except:
        print nextpage
    soup = BeautifulSoup(htmltext)

    for tag in soup.findAll("div", { "class" : "resultsPane"}):
        if tag.contents[1].string is not None and tag.contents[3].string is not None: 
            wurl = tag.contents[3].string
            tmplist = wurl.split("/")
            if len(tmplist) == 1:
                Website(website_name=tag.contents[1].string, website_url=tag.contents[3].string).save()
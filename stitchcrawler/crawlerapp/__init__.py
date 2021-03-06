import urlparse
import urllib
from bs4 import BeautifulSoup
from crawlerapp.models import Website

# search engine url with the search query 
url = 'http://www.webcrawler.com/search/web?qsi=%s1&q=onlinedatingsites&aid=2aecfd91-196c-4811-a88a-f0fd033abf7b&ridx=3&fcoid=4&fcop=results-bottom&fpid=2'

# the page number of the search results produced
num = 0

# can keep it as True, but its the init - don't want to keep waiting for that long
while num < 20:
    try:
        # get the qsi=01 -- 11 -- 21 -- 31 -- 41 and so on...
        nextpage = url % num
        num += 1
        htmltext = urllib.urlopen(nextpage).read()
    except:
        print nextpage
    soup = BeautifulSoup(htmltext)

    for tag in soup.findAll("div", { "class" : "resultsPane"}):
        if tag.contents[1].string is not None and tag.contents[3].string is not None: 
            wurl = tag.contents[3].string
            # if the url contains a /, e.g. www.abc.com/review/or/article its probably an article
            tmplist = wurl.split("/")
            if len(tmplist) == 1:
                Website(website_name=tag.contents[1].string, website_url=tag.contents[3].string).save()
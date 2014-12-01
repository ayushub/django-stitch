from django.shortcuts import render
from crawlerapp.models import Website

# Ayush added - views for displaying the crawled sites

from django.http import HttpResponse

def index(request):
	latest_website_list = Website.objects.all()
	output = '\n '.join([p.website_name for p in latest_website_list])
	return HttpResponse(output)

def detail(request, website_id):
	return HttpResponse("You're looking at %s website" % website_name)

def results(request, website_id):
	response = "You're looking at the results of %s website"
	return HttpResponse(response % website_name)

# Edit ends

from django.contrib import admin

#Ayush added - make app modifiable through admin ui
from crawlerapp.models import Website

admin.site.register(Website)
#Edit ends

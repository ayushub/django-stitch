from django.db import models

#Model for the required crawler
class Website(models.Model):
	website_name = models.CharField(max_length=200)
	website_url  = models.CharField(max_length=3000)
	
	def __unicode__(self):
		return self.website_name

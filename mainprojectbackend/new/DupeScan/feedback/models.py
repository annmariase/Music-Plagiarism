from __future__ import unicode_literals

from django.db import models

class feedback(models.Model):
	Your_name=models.CharField(max_length=120)
	Your_email=models.CharField(max_length=120)
	Your_message=models.TextField()
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

	def _unicode(self):
		return self.title

	def _str_(self):
		return self.title
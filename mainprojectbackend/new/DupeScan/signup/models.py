from __future__ import unicode_literals

from django.db import models

from DupeScan.settings import BASE_DIR

# Create your models here.
class signup(models.Model):
	Name=models.CharField(max_length=120)
	Subname=models.CharField(max_length=120)
	Address=models.CharField(max_length=120)
	Phone_Number=models.CharField(max_length=120)
	E_mail=models.CharField(max_length=120,primary_key=True)
	Password=models.CharField(max_length=120)
	Repeat_password=models.CharField(max_length=120)


	def __unicode__(self):
		return self.Name

	def __str__(self):
		return self.Name

def user_directory_path(instance, filename):
	return '{2}/static/{0}/{1}'.format(instance.userId, filename,BASE_DIR)


class Track(models.Model):
	userId = models.ForeignKey(signup, on_delete=models.CASCADE)
	midiFile = models.FileField(upload_to=user_directory_path)
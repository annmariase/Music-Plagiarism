# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class signin(models.Model):
	Username=models.CharField(max_length=120)
	Password=models.CharField(max_length=120)

	def __unicode__(self):
		return self.Username

	def __str__(self):
		return self.Username


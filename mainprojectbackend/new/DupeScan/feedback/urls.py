from django.conf.urls import url
from django.contrib import admin
from feedback.views import (
	homepage
	)

urlpatterns = [
	url(r'^$',homepage)
   ]
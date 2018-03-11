# DupeScan URL Configuration
from django.conf.urls import url
from django.contrib import admin
from .views import (
sign_up
	)

urlpatterns = [
	url(r'^$',sign_up),
]

# urlpatterns = []
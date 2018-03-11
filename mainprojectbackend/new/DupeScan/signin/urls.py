from django.conf.urls import url
from django.contrib import admin
from .views import sign_in, homepage, logout, tracks
from signup.views import uploadTrack

urlpatterns = [
	url(r'home/$', homepage),
	url(r'logout/$', logout),
	url(r'upload/$', uploadTrack),
	url(r'tracks/$', tracks),
	url(r'$', sign_in)
]

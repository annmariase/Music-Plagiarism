from django.shortcuts import render,redirect
from signup.models import signup
#from django.http import HttpResponse,JsonResponse
from django.db.models import F
from DupeScan.settings import STATICFILES_DIRS
import os

from signup.models import Track

# Create your views here.

def sign_in(request):
	print "signin"
	if request.method == 'GET':
		return render(request,"signin.html",{})
	else:
		print request.POST
		results = signup.objects.filter(E_mail=request.POST['username'])
		print results
		if len(results)!=0:
			if(results[0].Password!=request.POST['password']):
				return redirect('/')
			else:
				request.session['loggedin'] = True
				request.session['userId'] = results[0].Name
				return redirect('/signin/home/')
		return redirect('/')

def logout(request):
	request.session['loggedin'] = False
	request.session['userId'] = None
	return redirect('/')

def homepage(request):
	print "home"
	if request.session['loggedin']:
		return render(request, 'index2.html', {})
	return redirect('/')

def tracks(request):
	if request.session['loggedin']:
		tracks = Track.objects.all()
		table = [ track.midiFile.name.split('/')[-1] for track in tracks  ]

		return render(request, 'table.html', {'library': table})
	return redirect('/')
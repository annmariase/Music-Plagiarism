from django.shortcuts import render,redirect
from .models import signup as SIGNUP, Track

# Create your views here.
def sign_up(request):
	if request.method == 'GET':
		return render(request,"signup.html",{})
	else:
		signup = SIGNUP(Name=request.POST['name'],
			Subname=request.POST['subname'],
			# Address=request.POST['address'],
			Phone_Number= request.POST['telno'],
			E_mail= request.POST['email'],
			Password= request.POST['password']) 	
		signup.save()
		request.session['loggedin'] = True
		return redirect('/signin/home/')
	
def uploadTrack(request):
	user = SIGNUP.objects.get(Name=request.session['userId'])
	print dir(request.FILES['upload'])
	print request.FILES['upload'].__repr__
	if request.method == 'POST':
		track = Track(userId = user, midiFile = request.FILES['upload'])
		track.save()
		# if request.FILES.get('upload').name == '':
			#asdasd
		name = request.FILES.get('upload').name
		
		return render(request, 'final.html', { 'percentage': '90%', 
			'yoursong': request.FILES.get('upload').name,
			'similarsong': 'amrdiab' })
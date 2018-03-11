from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.db.models import F
# from signin.models import Fund

# Create your views here.
#def webapp_create(request):
	#return HttpResponse()

#def webapp_detail(request): #retrieve
#	return HttpResponse("<h1>detail</h1>")

def homepage(request):    #list items
	if(request.method=='GET'):
		if(request.session.get('loggedin')):
			print "go home"
			return redirect('/signin/home/')
		return render(request,"index.html",{})
	else:
		print request.POST
		email = request.POST.get('email')
		name = request.POST.get('name')
		message = request.POST.get('message')
		send_mail('Feedback from '+name,
			message+'\nName: '+name+'\nEmail: '+email,
			'ds.professional.dupescan@gmail.com',
			['ds.professional.dupescan@gmail.com'],
			fail_silently=False)
		return redirect('/')


def testmail(request):
	send_mail('Subject here', 'test','ds.professional.dupescan@gmail.com',['ds.professional.dupescan@gmail.com'], fail_silently=False)
	return HttpResponse("sent mail")

#ef webapp_delete(request):
#	return HttpResponse("<h1>delete</h1>")

#from django.core.mail import send_mail
#end_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
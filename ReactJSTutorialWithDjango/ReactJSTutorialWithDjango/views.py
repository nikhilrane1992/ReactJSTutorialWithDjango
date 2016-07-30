from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render_to_response

def landing_page(request):
	return render_to_response('Templates/landing_page.html')

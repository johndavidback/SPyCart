# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

import SPyCart.cart

def index(request):

	return render_to_response('cart/index.html')
	
def catalog(request):

	return render_to_response('cart/catalog.html')
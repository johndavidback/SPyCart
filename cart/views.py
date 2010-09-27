# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from SPyCart.cart.cart import Cart

def index(request):
	x = Cart(request)
	
	x.addItem(request, 'item1', 1, 1.5)
	return render_to_response('cart/index.html', {'cart_total': x.getTotal(request)})
	
def catalog(request):

	return render_to_response('cart/catalog.html')
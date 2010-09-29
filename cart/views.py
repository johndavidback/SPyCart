# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from SPyCart.cart.models import Product

from SPyCart.cart.cart import Cart

def index(request):
	x = Cart(request)
	
	x.addItem(request, 'item1', 1, 1.5)
	return render_to_response('cart/index.html', {'cart_total': x.getTotal(request)})
	
def catalog(request):
	p = Product.objects.all()
	return render_to_response('cart/catalog.html', {'products': p})
	
def product(request, product_id):
	p = Product.objects.get(pk=product_id)
	return render_to_response('cart/product.html', {'p': p})
class Cart:
	""" This is the cart class, to be used for the cart.  Make sense? """
	
	# borrowed the init stuff from jonathancurrin/python-cart, Thanks jonathan!
	_cart = {}
	
	def __init__(self, request):
		self.request = request
		
		if 'cart' in self.request.session.keys():
			self._cart = self.request.session['cart']
		else:
			self._cart['cart_total'] = 0.0
			self._cart['item_count'] = 0
			self._cart['items'] = {}
			
	
	def getTotal(self, request):
		return self._cart['cart_total']
		
	def addItem(self, request, name, qty, amount):

		self._cart['cart_total'] += qty * amount
		self._cart['item_count'] += 1
		
		self.save()
		
		pass
		
	def save(self):
		
		pass
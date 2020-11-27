from django.shortcuts import render

# Create your views here.
def index(request):
	
	context = {
		'title': 'Cart Page'
	}
	
	return render(request, 'cart/index.html', context)

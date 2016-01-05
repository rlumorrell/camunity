from django.shortcuts import render

# Create your views here.

def landing_view(request):
	return render(request, 'landing_view.html', {})

def about(request):
	return render(request, 'about.html',{})


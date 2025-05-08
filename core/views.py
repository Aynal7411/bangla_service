from django.shortcuts import render

# Create your views here.

def landing_home_page(request):
    return render(request, 'core/landing_page.html')

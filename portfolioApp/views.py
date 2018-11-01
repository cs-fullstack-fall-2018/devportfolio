from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolioApp/base.html')

def aboutme(request):
    return render(request, 'portfolioApp/about.html')

def project(request):
    return render(request, 'portfolioApp/project.html')

def contact(request):
    return render(request, 'portfolioApp/contact.html')
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'portfolioApp/base.html')

def aboutme(request):
    return render(request, 'portfolioApp/about.html')

def project(request):
    return render(request, 'portfolioApp/project.html')

def contact(request):
    return render(request, 'portfolioApp/contact.html')

def contactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'portfolioApp/contact.html',{'form':form})
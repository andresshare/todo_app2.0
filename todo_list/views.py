from django.shortcuts import render

# Create your views here.
def home(request):
    return (request, 'home.html', {})

def about(request):
    return(request, 'about.html', {})
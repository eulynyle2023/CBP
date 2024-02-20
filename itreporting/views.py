from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


def home(request): 

    # return HttpResponse('<h1>Student IT Services - Home</h1>') 
    return render(request, 'itreporting/home.html')



def about(request): 

    return HttpResponse('<h1>Student IT Services - About</h1>') 


def contact(request): 

    return HttpResponse('<h1>Student IT Services - Contact</h1>') 
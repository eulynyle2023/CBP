from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


def home(request): 

    print("the requedst is", request)

    # return HttpResponse('<h1>Student IT Services - Home</h1>') 
    return render(request, 'itreporting/home.html')



def about(request): 

    return render(request, 'itreporting/about.html', {'title': 'About'}) 


def contact(request): 

    return render(request, 'itreporting/contact.html', {'title': 'Contact'})
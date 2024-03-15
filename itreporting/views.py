from django.shortcuts import render
from django.http import HttpResponse 
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.


def home(request): 

    print("the requedst is", request)

    # return HttpResponse('<h1>Student IT Services - Home</h1>') 
    return render(request, 'itreporting/home.html')



def about(request): 

    return render(request, 'itreporting/about.html', {'title': 'About'}) 


def contact(request): 

    return render(request, 'itreporting/contact.html', {'title': 'Contact'})



def A(request):
    return render(request, 'itreporting/A.html', {'title': 'A'})



def B(request):
    return render(request, 'itreporting/B.html', {'title': 'B'})



def report(request):
    # Get all reported issues

    issues = Issue.objects.all()
    context = {'issues': issues, 'title': 'Issues Reported'}

    # Calculate even/odd flag in the view
    for index, issue in enumerate(issues):
        issue.is_even = index % 2 == 0

    return render(request, 'your_template.html', context)
    # daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}


    # return render(request, 'itreporting/report.html', daily_report)




class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 10  # Optional pagination
    



class UserPostListView(ListView): 

    model = Issue
    template_name = 'itreporting/issues_users.html' 
    context_object_name = 'issues'
    paginate_by = 5


    def get_queryset(self):

        user=get_object_or_404(User, username=self.kwargs.get('username'))

        return Issue.objects.filter(author=user).order_by('-date_submitted')


class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'



class PostCreateView(LoginRequiredMixin, CreateView):

    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 

        form.instance.author = self.request.user
        return super().form_valid(form)
    



    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 

    model = Issue

    fields = ['type', 'room', 'details']
    
    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Issue

    success_url = '/report'
    
    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author

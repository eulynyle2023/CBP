from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomLoginForm


# Create your views here.



class CustomLoginView(LoginView):
    
    template_name = '../templates/login.html'  # Use your custom login template
    # form = CustomLoginForm  # Use the custom login form class
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy("itreportings:home")
  



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request)
        if form.is_valid():

            print(form.data)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!') 
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Student Registration'})





@login_required 
def profile(request):
    
    if request.method == 'POST':
        
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, 'Your account has been successfully updated!')
                return redirect('profile')
    else:
                
            u_form = UserUpdateForm(instance = request.user) 
            p_form = ProfileUpdateForm(instance = request.user.profile) 
            context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'} 
            return render(request, 'users/profile.html', context) 
    
  





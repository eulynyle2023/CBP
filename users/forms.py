
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm






class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label='Email address', help_text='Your SHU email address.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']






class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




class CustomLoginForm(forms.Form):

    print('this is nw')

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'required': True, 'class': 'user-box', 'placeholder': 'Username'}))
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'required': True, 'class': 'user-box', 'placeholder': 'Password'}))

    def clean(self):
        print('this s neww')
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)  # If using User model (replace with your model)
            except User.DoesNotExist:
                user = None

            if user and user.check_password(password):
                return cleaned_data  # Authentication successful
            else:
                raise forms.ValidationError('Invalid username or password.')
            
        print(cleaned_data)

        return cleaned_data  # Raise ValidationError for other cases (e.g., missing fields)
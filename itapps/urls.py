"""
URL configuration for itapps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from itreporting import views
from django.contrib.auth import views as auth_views
import users.views as user_views
from users.views import register as reg1
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home', views.home, name = 'home'), 
    path('', include('itreporting.urls')),  
    # path('register', users.views.register, name="register"),  
    path('register', reg1, name="register"),  
    # path('', include('itreporting.urls')),  
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile', user_views.profile, name = 'profile'), 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path,include
from blog.views import index,post_detail,get_ip
from blango_auth.views import profile
import debug_toolbar
from blango_auth.forms import BlangoRegistrationForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path("post-detail/<str:slug>",post_detail,name="post_detail"),
    path("ip/",get_ip),
    #path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/",profile,name="profile"),
    path("accounts/login/",profile,name="login"),
    path("accounts/register/",RegistrationView.as_view(form_class=BlangoRegistrationForm),name="django_registration_register"),
    path("accounts/", include("django_registration.backends.activation.urls")),
]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
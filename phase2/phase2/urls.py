"""phase2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mysite.views import register
from mysite.views import login
from mysite.views import logout
from mysite.views import dummy
from mysite.views import move

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^dummy/', dummy),
    url(r'^move/', move),
]

"""new URL Configuration

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
from django.contrib import admin
from django.urls import path
from tool.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',title_list),
    path('detail/<int:title_number>/',get_details,name='detail'),
    path('make_title/',make_title),
    path('delete_title/<int:title_number>/',delete_title,name='delete_title'),
    path('make_content/<int:title_number>/',make_content,name='make_content'),
    path('delete_content/<int:title_number>/',delete_content,name='delete_content'),
]

"""REPLIQS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Company import views as company_views
from Assets import views as assets_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',company_views.home,name='home'),
    path('register/',company_views.register,name='register'),
    path('login/',company_views.login,name='login'),
    path('assets/',company_views.assets,name='assets'),
    path('assign/',assets_views.assign,name='asset_assign'),
    path('logout/',company_views.logout,name='logout'),
    path('addEmployee/',company_views.addEmployee,name='addEmployee'),
    path('addAsset',assets_views.addAsset,name='addAsset')
]

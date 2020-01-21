"""categoriesAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet


router = DefaultRouter(trailing_slash=False)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', lambda r: redirect('/api/v1/categories')),
    path('api/', lambda r: redirect('/api/v1/')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

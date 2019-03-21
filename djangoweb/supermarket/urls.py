from django.contrib import admin
from django.urls import path
from supermarket import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('supermk', views.supermk),
    path('data', views.data, name='data'),
    path('d3sample', views.d3sample),
]

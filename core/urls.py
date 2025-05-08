from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_home_page, name='home_page'),
]
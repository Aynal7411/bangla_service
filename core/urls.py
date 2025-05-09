from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_home_page, name='home_page'),
    path('post/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
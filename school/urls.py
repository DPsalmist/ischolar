from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('payfees/', views.payfees, name='payfees'),
]
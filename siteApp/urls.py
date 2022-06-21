from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('seventeen/', views.seventeen, name='seventeen'),
    path('apink/', views.apink, name='apink'),
    path('lostark/', views.lostark, name='lostark'),
]
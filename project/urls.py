from django.urls import path 
from . import views
# URL Configuration
urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('show/<int:id>', views.show, name="show"),
    path('alternatives/', views.alternatives, name='alternatives'),
    path('aboutus/', views.aboutus, name='aboutus')
]
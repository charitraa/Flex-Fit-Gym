from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('signin', views.login, name="signin"),
    path('signup', views.registration, name="signup"),
    path('customer', views.customerdashboard, name="customer"),
    path('admindashboard', views.admindashboard, name="admindashboard"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
]

from django.urls import path
from . import views

urlpatterns = [

    path('', views.LandingPage.as_view(), name="LandingPage"),
    

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name="resumesite-home"),
    path('about/', views.about, name="resumesite-about")

]
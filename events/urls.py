from django.urls import path
from . import views
urlpatterns = [
	
     path('home', views.home , name="home"),
     path('', views.come , name="come"),
     # path('', views.participant_csv , name="participant_csv"),
    
]
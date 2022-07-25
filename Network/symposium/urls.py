from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('model/<slug:pk>', views.model, name='model'),
    path('exhibition', views.exhibition, name='exhibition'),
    path('lobby', views.lobby, name='lobby'),
]

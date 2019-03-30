#Aquí estamos importando la función de Django path y todos nuestras views desde la aplicación blog
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

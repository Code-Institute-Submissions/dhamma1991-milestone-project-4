from django.urls import path

from . import views

app_name = 'stats'
urlpatterns = [
    path('', views.get_stats, name='get_stats'),
]
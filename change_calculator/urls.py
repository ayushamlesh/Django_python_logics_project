from django.urls import path
# importing view
from . import views
urlpatterns = [
    # path for the sum.html file
    path('', views.index, name='index'),
    # for change calculator
    path('forms/', views.forms, name='forms'),
    path('forms/ans/', views.calculate_ride, name='calculate'),

]

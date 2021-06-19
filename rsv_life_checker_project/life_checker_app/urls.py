from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('r/', views.check, name='check'),
    path('s/', views.check_2, name='check_2'),
    path('myajaxtest/', views.testcall),
    # path('r/', views.check, name='check'),
]
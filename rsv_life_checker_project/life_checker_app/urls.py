from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('r/', views.check, name='check'),
    path('myajaxtest/', views.testcall),
    # path('r/', views.check, name='check'),
]
from django.urls import path
from entries import views

urlpatterns = [
    path('<c_id>/', views.index),
    path('<c_id>/addd/', views.addd, name='add')
]

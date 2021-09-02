from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reminder/', views.add_reminder, name='add_reminder'),
    path('view/', views.reminderview, name='reminderview'),
    path('update/<int:pk>', views.updatereminder, name='updatereminder'),
    path('delete/<int:pk>', views.deletereminder, name='deletereminder')

    ]

from django.urls import path

from . import views

urlpatterns = [
    path('<c_id>/', views.index),
    path('adddd', views.addTodo, name='adddd'),
    path('complete/<todo_id>/', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]

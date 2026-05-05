from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_property, name='add'),
    path('delete/<int:id>/', views.delete_property, name='delete'),
    path('predict/', views.predict, name='predict'),
]
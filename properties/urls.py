from django.urls import path
from . import views
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_property, name='add'),
    path('delete/<int:id>/', views.delete_property, name='delete'),
    path('predict/', views.predict, name='predict'),
    path('signup/', signup_view, name='signup'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

]

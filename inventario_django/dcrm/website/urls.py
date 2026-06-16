from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registro/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('add_record/', views.add_record, name='add_record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
    # Gestión de Usuarios
    path('users/', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('update_user/<int:pk>/', views.user_update, name='user_update'),
    path('delete_user/<int:pk>/', views.user_delete, name='user_delete'),
    path('add_user/', views.add_user, name='add_user'),
]
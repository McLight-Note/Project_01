from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.product_create_view, name='product_create'),
    path('list/', views.product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
    path('decrease/<int:product_id>/', views.decrease_quantity_view, name='decrease_quantity'),
    path('login/', auth_views.LoginView.as_view(template_name='remProd/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
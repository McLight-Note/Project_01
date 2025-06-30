from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('health/', views.health_check, name='health_check'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create/', views.product_create_view, name='product_create'),
    path('list/', views.product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
    path('decrease/<int:product_id>/', views.decrease_quantity_view, name='decrease_quantity'),
    path('quantity/<int:product_id>/', views.update_quantity_view, name='update_quantity'),
    path('login/', auth_views.LoginView.as_view(template_name='remProd/login.html', next_page='dashboard'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
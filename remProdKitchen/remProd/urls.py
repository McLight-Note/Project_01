from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.product_create_view, name='product_create'),
    path('list/', views.product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
    path('decrease/<int:product_id>/', views.decrease_quantity_view, name='decrease_quantity'),
    path('export/', views.export_inventory_view, name='export_inventory'),
    path('export-text/', views.export_text_view, name='export_text'),
    path('import/', views.import_inventory_view, name='import_inventory'),
    path('backup/', views.backup_inventory_view, name='backup_inventory'),
]
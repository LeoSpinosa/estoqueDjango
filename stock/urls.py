from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search-product/', views.search_product, name='search-product'),
    path('stockless/', views.view_stockless, name='stockless'),
    path('add-product/', views.add_product, name='add_product'),
    path('products_detail/<int:id>/', views.products_detail, name='products_detail'),
    path('delete-product/<int:id>/', views.delete_product, name='delete-product'),
    path('sell-product/<int:id>/', views.sell_product, name='sell-product'),
]
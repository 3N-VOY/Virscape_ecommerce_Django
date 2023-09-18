from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('<slug:category_slug>/<slug:slug>/', views.view_item, name='view_item'),
    path('search/', views.search_item, name='search_results'),
    path('<slug:slug>', views.view_category, name="category_view" ),

]
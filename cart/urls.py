from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('create-checkout-session/', views.create_checkout_session),
    path('payment_success/', views.payment_success, name="payment_success"),
    path('payment-failed/', views.payment_cancel, name="payment-failed"),
    
    
    
]




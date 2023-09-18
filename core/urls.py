from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('shipping-return/', views.shipping_return, name="shipping_return"), 
    path('terms-of-service/', views.terms_service, name="terms_service"),
]

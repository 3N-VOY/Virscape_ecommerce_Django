from django.contrib import admin
from django.urls import path
from .  import views



urlpatterns = [
    path("register/", views.signup, name="register"),
    path('login/', views.loginpage, name='login'),
    path("logout/", views.logoutUser, name="logoutuser"),
    path("my-account/<str:pk>", views.myaccount, name="my_account"),
    path('favourites/<int:id>', views.add_favourites, name="add_favourites"),
    path('my-account/favourites/', views.favourites_list, name="favourites_list"),
    path('my-account/edit-profile/<int:id>', views.edit_profile, name="edit_profile"),
]

app_name = 'userprofiles'
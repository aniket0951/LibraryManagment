from django.contrib import admin
from django.urls import path
from .views import OpenLibrary, UserLogin,Registration, AddNewBook, AllBookClass

urlpatterns = [
    path('openlibrary/', OpenLibrary, name='open'),
    path('userlogin/', UserLogin, name='user_login'),
    path('registration/<str:tag>/', Registration, name='registration'),
    path('addNewBook/<str:tag>/', AddNewBook, name='addNewBook'),
    path('allBooks/', AllBookClass.as_view(), name='allBookClass'),
]
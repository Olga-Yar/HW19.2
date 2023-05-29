from django.urls import path

from catalog.views import index, contact

urlpatterns = [
    path('home', index),
    path('contact', contact)
]

from django.urls import path, include
import debug_toolbar
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
]

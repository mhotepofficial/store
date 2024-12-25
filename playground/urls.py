from django.urls import path, include
import debug_toolbar
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('__debug__/', include(debug_toolbar.urls)),
]

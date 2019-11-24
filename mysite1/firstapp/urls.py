
from django.urls import path
from firstapp import views as first

urlpatterns = [
    path('as/',first.index),
    path('login/',first.user_login)
]

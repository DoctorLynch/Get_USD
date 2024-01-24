from django.urls import path

from dollar_rate.views import index

urlpatterns = [
    path('', index),
]
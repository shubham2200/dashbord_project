from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('',dashbord,name='dashbord'),
    path('products/',products,name='products'),
    path('costomer/',costomer,name='costomer'),

]

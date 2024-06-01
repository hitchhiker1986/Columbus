from django.urls import path
from columbus.views import *

app_name = 'columbus'
urlpatterns = [
    path('home/', home, name='home'),
]
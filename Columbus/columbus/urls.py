from django.urls import path
from columbus.views import *

app_name = 'columbus'
urlpatterns = [
    path('home/', home, name='home'),
    path('apartment_list', apartment_list, name='apartment_list'),
    path('owner_list/', owner_list, name='apartment_list'),
    path('tenant_list/', tenant_list, name='apartment_list'),
    path('apartment_create', apartment_show_and_modify, name='apartment_show'),
    path('apartment_show/<int:apt_id>', apartment_show_and_modify, name='apartment_show'),
    path('tenant_show/<int:tenant_id>', tenant_show_and_modify, name='tenant_show'),
    path('owner_show/<int:owner_id>', owner_show_and_modify, name='owner_show'),
]
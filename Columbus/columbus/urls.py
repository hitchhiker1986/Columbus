from django.urls import path
from columbus.views import *

app_name = 'columbus'
urlpatterns = [
    path('home/', home, name='home'),
    path('apartment_list/', apartment_list, name='apartment_list'),
    path('owner_list/', owner_list, name='owner_list'),
    path('tenant_list/', tenant_list, name='tenant_list'),
    path('task_list/', task_list, name='task_list'),
    path('apartment_create/', apartment_create, name='apartment_create'),
    path('tenant_create/', tenant_create, name='tenant_create'),
    path('owner_create/', owner_create, name='owner_create'),
    path('task_create/', task_create, name='task_create'),
    path('apartment_show/<int:apt_id>/', apartment_show_and_modify, name='apartment_show'),
    path('tenant_show/<int:tenant_id>/', tenant_show_and_modify, name='tenant_show'),
    path('owner_show/<int:owner_id>/', owner_show_and_modify, name='owner_show'),
    path('task_show/<int:task_id>/', task_show_and_modify, name='task_show'),
    path('dict_years/', dict_years, name='dict_years'),
    path('dict_list/<int:year>', dict_list, name='dict_list'),
path('apartment/dict/<int:pk_id>', dict_view, name='dict'),
]
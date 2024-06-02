from django.contrib import admin
from .models import Apartment, Owner, Tenant, Utility, Task
# Register your models here.

admin.site.register(Apartment)
admin.site.register(Owner)
admin.site.register(Tenant)
admin.site.register(Utility)
admin.site.register(Task)
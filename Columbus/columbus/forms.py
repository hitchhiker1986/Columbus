from django import forms
from .models import *
from django.db import models


class DictForm(forms.ModelForm):
    class Meta:
        model = Utility
        fields = ('current', )


class CheckForm(forms.ModelForm):
    class Meta:
        model = CheckHistory
        fields = ('cleaning', 'smoke', 'damage', 'animal', 'equipment_damage', 'not_allowed_tenants', 'description',)


class SentContractForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('sent_contract', )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')

    widgets = {
        'start_day': forms.DateInput(),
        'end_day': forms.DateInput(),
    }


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('__all__')

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('__all__')


class ApartmentBaseDetailsForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('address', 'zip', 'city', 'district', 'topographical_nr', 'floor', 'size', 'rooms', 'halfrooms', 'balcony_size', 'furnished', 'is_active')


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('__all__')


class UtilityForm(forms.ModelForm):
    class Meta:
        model=Utility
        fields = ('__all__')

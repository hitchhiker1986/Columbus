from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import Tab, TabHolder
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

class ApartmentForm_old(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('__all__')


class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper


class ApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = ('__all__')
    """
    address = forms.CharField(required=True, max_length=30)
    zip = forms.IntegerField(required=True, initial=0)
    district = forms.CharField(max_length=6, required=False)
    topographical_nr = forms.CharField(max_length=20, required=False)
    floor = forms.CharField(max_length=10, required=False)
    city = forms.CharField(max_length=30, required=True)
    owner = forms.ModelMultipleChoiceField(queryset=Owner.objects.all(), required=True)
    tenant = forms.ModelMultipleChoiceField(queryset=Tenant.objects.all(), required=False)
    size = forms.IntegerField(required=True, initial=0)
    rooms = forms.IntegerField(required=True, initial=1)
    halfrooms = forms.IntegerField(required=True)
    balcony_size = forms.CharField(required=True, max_length=20)
    furnished = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)
    price = forms.IntegerField(required=True)
    currency = forms.ChoiceField(choices=[('EUR', 'Euro'), ('HUF', 'Forint'),], required=True, initial='HUF')
    deposit = forms.IntegerField(required=False)
    overhead = forms.IntegerField(required=False)
    premiumPercentage = forms.IntegerField(required=True)
    premium = forms.FloatField(required=True, initial=0)
    next_check = forms.IntegerField(required=True, initial=1)
    check_status = forms.BooleanField(required=True, initial=True)
    last_check = forms.DateField(required=False)
    # documents
    sent_contract = forms.FileField(required=False)
    signed_contract = forms.FileField(required=False)
    leave_statement = forms.FileField(required=False)
    takeover_checklist = forms.FileField(required=False)
    child_acceptance_statement = forms.FileField(required=False)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TabHolder(
                Tab('Alapadatok',
                    'address',
                    'city',
                    'zip',
                    'district',
                    'topographical_nr',
                    'floor',
                    'size',
                    'rooms',
                    'halfrooms',
                    'balcony_size',
                    'furnished',
                    'is_active',
                ),
                Tab('Bérlők',
                    'tenant',
                ),
                Tab('Tulajdonosok',
                    'owner',
                    ),
                Tab('Pénzügyek',
                    'price',
                    'deposit',
                    'overhead',
                    'premiumPercentage',
                    'premium',
                    ),
                Tab('Szerződések',
                    'sent_contract',
                    'signed_contract',
                    'leave_statement',
                    'takeover_checklist',
                    'child_acceptance_statement'
                    ),
            )
        )
        self.helper.layout.append(Submit('submit', 'Submit'))

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('__all__')


class UtilityForm(forms.ModelForm):
    class Meta:
        model=Utility
        fields = ('__all__')

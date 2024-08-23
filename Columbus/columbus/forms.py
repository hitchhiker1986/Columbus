from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from crispy_forms.bootstrap import Tab, TabHolder
from django.forms import inlineformset_factory


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

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
            'start_day': forms.DateInput(attrs={'type': 'date'}),
            'end_day': forms.DateInput(attrs={'type': 'date'}),
        }


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('__all__')

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('__all__')
        labels = {
            'name': "Név",
            'owner_email': "E-mail cím",
            'country': "Ország",
            'city': "Város",
            'zip': "Irányítószám",
            'address': "Cím",
            'phone': "Telefonszám",
            'birth_name': "Születési név",
            'persID': "Személyigazolvány szám",
            'taxID': "Adószám",
            'iban': "Bankszámlaszám",
            'is_company': "Cég",
            'active_owner': "Aktív",
            'owner_company_registration_number': "Cégjegyzékszám",
            'owner_company_tax_nr': "Cég adószáma",
            'owner_company_contact_name': "Kapcsolattartó neve",
            'owner_company_contact_phone': "Kapcsolattartó telefonszáma",
            'owner_company_contact_email': "Kapcsolattartó E-mail címe",
        }

    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    'owner_email',
                    'country',
                    'city',
                    'zip',
                    'address',
                    'phone',
                    'birth_name',
                    'persID',
                    'taxID',
                    'iban',
                    'is_company',
                    'active_owner',
                    css_class = 'default_div'
                ),
                Div(
                    'owner_company_registration_number',
                    'owner_company_tax_nr',
                    'owner_company_contact_name',
                    'owner_company_contact_phone',
                    'owner_company_contact_email',
                    css_class = 'company_div'
                ),
                css_class = 'owners_div'
            )
        )

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
        labels = {'address':"Cím",
                  'zip': "Irányítószám",
                  'district': "Kerület",
                  'topographical_nr': "Helyrajzi szám",
                  'floor': "Emelet",
                  'city': "Város",
                  'Owner': "Tulajdonos",
                  'tenant': "Bérlö",
                  'size': "Alapterület",
                  'rooms': "Szobaszám",
                  'halfrooms': "Félszobák",
                  'balcony_size: "Erkélyek (m2)",'
                  'furnished': "Bútorozott",
                  'is_active': "Aktív",
                  'price': "Bérleti díj",
                  'currency': "Pénznem",
                  'deposit': "Kaució",
                  'overhead': "Rezsi",
                  'premiumPercentage': "Jutalék (%)",
                  'premium': "Jutalék",
                  'next_check': "Következö ellenörzés",
                  'sent_contract': "Elküldött szerzödés",
                  'signed_contract': "Aláírt szerzödés",
                  'leave_statement': "Kiköltözési nyilatkozat",
                  'takeover_checklist': "Átadási jegyzökönyv",
                  'child_acceptance_statement': "Gyerekbefogadási nyilatkozat",
                  }

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
                    'next_check',
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


class UtilityForm(forms.ModelForm):
    class Meta:
        model=Utility
        fields = ('__all__')


# BillFormSet = inlineformset_factory(CashOutBill, Bill, fields=['bill_nr', 'amount'], can_delete=True, can_order=True)

class CashOutBillForm(forms.ModelForm):
    class Meta:
        model = CashOutBill
        fields = ('__all__')
        # formset = BillFormSet(instance=CashOutBill)

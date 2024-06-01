from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from django.core import management
from datetime import datetime

# Create your views here.

"""
Views for non-functional pages, like home, thanks etc
"""
@login_required
def home(request):
    return render(request, 'home.html')

def thanks(request):
    return render(request, 'thanks.html')

"""
Views related to Apartment(s)
"""

@login_required
def apartment_list(request):
    apartments = {}
    if request.user.is_staff:
        apartments = Apartment.objects.all()

    if request.user.groups.filter(name="Tenants").exists():
        apartments = Apartment.objects.filter(tenant__user__username__contains=request.user)

    if request.user.groups.filter(name="Owners").exists():
        apartments = Apartment.objects.filter(owner__user__username__contains=request.user)

    return render(request, 'apartment/apartment_list.html', {'apartments': apartments})


@login_required
def apartment_show_and_modify(request, apt_id):
    apartment = Apartment.objects.get(pk=int(apt_id))
    form = ApartmentForm(instance=apartment)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            new_apartment = form.save(commit=False)
            new_apartment.save()
            # email().send

    return render(request, 'apartment/apartment_form.html', {'form': form})


def apartment_checkform(request, apt_id):
    apartment = Apartment.objects.get(id=apt_id)
    form = CheckForm(request.POST)
    ch = CheckHistory()

    check_result = True
    print(request.method)
    if request.method == "POST":
        print('it was just submitted')
        if form.is_valid():
            ch.checkDate = datetime.now()
            ch.cleaning = form.cleaned_data['cleaning']
            ch.smoke = form.cleaned_data['smoke']
            ch.damage = form.cleaned_data['damage']
            ch.equipment_damage = form.cleaned_data['equipment_damage']
            ch.animal = form.cleaned_data['animal']
            ch.not_allowed_tenants = form.cleaned_data['not_allowed_tenants']
            ch.description = form.cleaned_data['description']
            ch.save()
            #apartment.check_history.add(ch)
            for data in form.cleaned_data.values():
                print(data)
                if data is False:
                    check_result = False
                    break
            if check_result:
                management.call_command('create_check_tasks', apt_id)
            else:
                apartment.check_status = False
                apartment.save()
                management.call_command('create_check_tasks', apt_id)

            return HttpResponseRedirect("/thanks")

    return render(request, 'apartment/apartment_checkform.html', {'form': form})

"""
Views related to Owner(s)
"""

@login_required
def owner_list(request):
    owners = None
    if request.user.is_staff:
        owners = Owner.objects.all()

    if request.user.groups.filter(name="Owners").exists():
        owners = Owner.objects.filter(user__username__contains=request.user)
        for owner in owners:
            print(owner.user)

    return render(request, "owner_list.html", {'owners': owners})


@login_required
def owner_show_and_modify(request, owner_id):
    owner = Owner.objects.get(pk=int(owner_id))
    form = OwnerForm(instance=owner)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            new_owner = form.save(commit=False)
            new_owner.save()
            #email().send

    return render(request, 'owner/owner_form.html', {'form': form})
"""
Views related to Tenant(s)
"""
@login_required
def tenant_list(request):
    tenants = None

    if request.user.is_staff:
        print("admin is logged in")
        tenants = Tenant.objects.all()

    if request.user.groups.filter(name="Tenants").exists():
        tenants = Tenant.objects.filter(user__username__contains=request.user)

    for tenant in tenants:
        print(tenant.user.username)

    return render(request, 'tenant_list.html', {'tenants': tenants})


@login_required
def tenant_show_and_modify(request, tenant_id):
    tenant = Tenant.objects.get(pk=tenant_id)
    form = TenantForm(instance=tenant)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            new_tenant = form.save(commit=False)
            new_tenant.save()

    return render(request, 'tenant/tenant_form.html', {'form': form})


"""
Views related to Utilities(s)
"""

def dict_view(request, pk_id):
    if request.method == 'POST':
        utility = Utility.objects.get(id=pk_id)
        form = dict_form(request.POST, instance=utility)
        if form.is_valid():
            form.save()
            utility.set_current(request.POST['current'])
            utility.save()
            dh = DictHistory()
            dh.update_serial(utility.get_serial())
            dh.dict_value = request.POST['current']
            dh.save()
            email = EmailMessage(
                "Dict successful",
                str(utility.get_serial()) + " diktalasa sikeres volt. A meroora uj erteke: " + str(utility.get_current()),
                "papplaszlopft@gmail.com",
                {"papp.l@icloud.com"},
            )
            email.send()
            return HttpResponseRedirect("/test/")

        else:
            for error in form.errors:
                print(error)
            form = DictForm()
    else:
        form = DictForm(request.POST)
    return render(request, 'dict.html', {'form': form})



"""
Views related to Task(s)
"""
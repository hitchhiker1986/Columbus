from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Owner(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, default="")
    owner_email = models.EmailField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    birth_name = models.CharField(max_length=50, blank=True)
    persID = models.CharField(max_length=20, blank=True)
    taxID = models.CharField(max_length=15, blank=True)
    iban = models.CharField(max_length=40, blank=True)
    is_company = models.BooleanField(default=False)
    active_owner = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tenant(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50, default="")
    tenant_mail = models.EmailField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    birth_name = models.CharField(max_length=50, blank=True)
    persID = models.CharField(max_length=20, blank=True)
    taxID = models.CharField(max_length=15, blank=True)
    is_company = models.BooleanField(default=False)
    active_tenant = models.BooleanField(default=True)

    def __str__(self):
        return self.birth_name


class Apartment(models.Model):
    address = models.CharField(max_length=30, blank=True)
    zip = models.IntegerField(null=False, default=0, blank=True)
    district = models.CharField(max_length=6, default="", blank=True)
    topographical_nr = models.CharField(max_length=20, blank=True)
    floor = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    owner = models.ManyToManyField(Owner, related_name="apartment_owner", blank=True)
    tenant = models.ManyToManyField(Tenant, related_name="apartment_tenant", blank=True)
    size = models.IntegerField(default=0, blank=True)
    rooms = models.IntegerField(default=1, blank=True)
    halfrooms = models.IntegerField(default=0, blank=True)
    balcony_size = models.CharField(default="0", max_length=20, blank=True)
    furnished = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0, blank=True)
    currency = models.TextChoices('HUF', 'EUR')
    deposit = models.PositiveIntegerField(default=0)
    overhead = models.PositiveIntegerField(default=0)
    premiumPercentage = models.PositiveIntegerField(default=15,
                                                    validators=[MinValueValidator(0), MaxValueValidator(100)])
    premium = models.FloatField(default=0,
                                validators=[MinValueValidator(15000), MaxValueValidator(50000)])
    # utilities = models.ManyToManyField(Utility, blank=True)
    next_check = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True)
    check_status = models.BooleanField(default=True, blank=True)
    last_check = models.DateField(null=True, blank=True)
    # documents
    sent_contract = models.FileField(upload_to='', blank=True, null=True)
    signed_contract = models.FileField(upload_to='Documents', blank=True, null=True)
    leave_statement = models.FileField(upload_to='Documents/', blank=True, null=True)
    takeover_checklist = models.FileField(upload_to='Documents/', blank=True, null=True)
    child_acceptance_statement = models.FileField(upload_to='Documents/', blank=True, null=True)

    def __str__(self):
        return self.address

    def calculate_premium(self):
        calculated = (int(self.price) / 100) * int(self.premiumPercentage)
        if calculated > 50000:
            return 50000
        elif calculated < 15000:
            return 15000
        else:
            return calculated


class Utility(models.Model):
    serial = models.CharField(max_length=30)
    current = models.FloatField()
    dict_start_day = models.PositiveIntegerField(default=1)
    dict_end_day = models.PositiveIntegerField(default=7)
    provider = models.CharField(max_length=20 ,default="")
    utility_type = models.CharField(max_length=10, default="")
    utility_unit = models.CharField(max_length=5, default="")
    apartment = models.ForeignKey(
        Apartment,
        null=True,
        on_delete=models.CASCADE,
        related_name="apartment",)

    util_responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='util_responsible_user',
    )
    # photo = models.ImageField()


    def __str__(self):
        return self.serial

    def set_delta(self, num):
        self.delta = num

    def set_current(self, num):
        self.current = num

    def update_meter(self, new_current):
        self.current = new_current

    def get_current(self):
        return self.current

    def get_serial(self):
        return self.serial


class CheckHistory(models.Model):
    apt = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        null=True,
        related_name='Checkhistory_Apartment',
    )
    checkDate = models.DateField(auto_now_add=True)
    cleaning = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    damage = models.BooleanField(default=False)
    animal = models.BooleanField(default=False)
    equipment_damage = models.BooleanField(default=False)
    not_allowed_tenants = models.BooleanField(default=False)
    description = models.TextField(max_length=500, default=False)


class Task(models.Model):
    #kész status -> csak akkor lehet completed ha Szilvi leokézta
    class Status(models.TextChoices):
        PENDING = "Pending"
        ACTIVE = "Active"
        IN_PROGRESS = "In Progress"
        COMPLETED = "Completed"
        CLOSED = "Closed"
        EXPIRED = "Expired"
    # status ami alapjan kiertekelodik hogy kihez milyen gyakran kell menni (problemas-e)
    start_day = models.DateField()
    end_day = models.DateField()
    description = models.TextField(max_length=500,)
    title = models.TextField(max_length=50, )
    task_responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='task_responsible_user',
    )
    status = models.CharField(choices=Status, default=Status.PENDING, max_length=12)

    def __str__(self):
        return self.title


class DictHistory(models.Model):
    utility_serial = models.CharField(max_length=30)
    dict_date = models.DateField(auto_now_add=True)
    dict_value = models.FloatField()

    @classmethod
    def update_serial(self, serial):
        self.utility_serial = serial

    @classmethod
    def update_value(self, value):
        self.dict_date = value

class CashOutBill(models.Model):
    buyer_name = models.CharField(max_length=30)
    buyer_address = models.CharField(max_length=50)
    amount = models.FloatField()
    amount_written = models.CharField(max_length=50)
    cashier = models.CharField(max_length=30)
    creator = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)


"""
class Bill(models.Model):
    cashout_bill = models.ForeignKey(CashOutBill,
                                     on_delete=models.CASCADE,
                                     related_name='cashout_bill',
                                     null=True)
    bill_nr = models.CharField(max_length=50)
    amount = models.FloatField()

"""




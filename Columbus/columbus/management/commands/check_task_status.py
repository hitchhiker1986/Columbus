import os

from django.core.management.base import BaseCommand, CommandError
from columbus.models import *
from django.core.mail import EmailMessage
from django.core.mail import get_connection
import datetime

#from columbus.models import Utility, Task



class Command(BaseCommand):
    def handle(self,  *args, **options):
        for task in Task.objects.all():
            print(str(task.status == 'Pending' and task.start_day == datetime.date.today() + datetime.timedelta(days=5)))
            if task.status == 'Pending' and task.start_day == datetime.date.today() + datetime.timedelta(days=5):
                task.status = 'Active'
                task.save()

                email = EmailMessage(
                task.title + " - Státuszváltozás - a feladat aktív",
                "A " + str(task.id) + " számú feladat státusza megváltozott.",
                User.objects.get(username="admin").email,
                {task.task_responsible.email},
                 )

            if task.end_day < datetime.date.today():
                task.status = 'Expired'
                task.save()



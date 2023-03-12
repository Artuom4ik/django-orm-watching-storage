import os

from django.core.management import execute_from_command_line

import django
from datetime import datetime, timedelta
from tabulate import tabulate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())

from datacenter.models import Passcard, Visit

if __name__ == "__main__":
    table = []
    visits_sick = []
    name_patient = "Shelby Owens"
    date_disease = datetime(2023, 2, 8)
    delta = date_disease - timedelta(days=7)
    disease_passcard = Passcard.objects.get(owner_name=name_patient)
    dangerous_visits = Visit.objects.filter(entered_at__lte=date_disease, entered_at__gt=delta)
    disease_visits = dangerous_visits.filter(passcard=disease_passcard)
    for dangerous_visit in dangerous_visits:
        if dangerous_visit.passcard.owner_name == name_patient:
            continue
        for disease_visit in disease_visits:
            if dangerous_visit.entered_at <= disease_visit.entered_at <= dangerous_visit.leaved_at and dangerous_visit.entered_at <= disease_visit.leaved_at <= dangerous_visit.leaved_at:
                visits_sick.append(dangerous_visit)
    for visit_sick in visits_sick: 
        table.append(["Имя посетителя", visit_sick.passcard.owner_name])
        table.append(["Дата посещения", visit_sick.leaved_at])
    print(tabulate(table))
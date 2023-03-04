import os
import datetime

import django
from django.utils.timezone import localtime, timezone

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def get_duration(visit, passcard_visit):
    entered_at = localtime(passcard_visit.entered_at)
    date_now = localtime(datetime.datetime.now(timezone.utc))
    delta = date_now - entered_at
    return int(delta.seconds)


def format_duration(duration):
    hour = duration // 3600
    minutes = (duration % 3600) // 60
    return f"{hour}:{minutes}"


def storage_information_view(request):
    passcards = Passcard.objects.all()
    passcards_visit = Visit.objects.filter(leaved_at__isnull=True)
    active_passcards = Passcard.objects.filter(is_active=True)
    non_closed_visits = []
    for passcard_visit in passcards_visit:
        visit = passcard_visit.entered_at
        duration = get_duration(visit, passcard_visit)
        visits = {
            'who_entered': f'{passcard_visit.passcard}',
            'entered_at': f'{passcard_visit.entered_at}',
            'duration': f'{format_duration(duration)}',
        }
        non_closed_visits.append(visits)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

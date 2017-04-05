from django.shortcuts import render, redirect
from datetime import datetime

from .models import StatiscticsHit

def index(request):
    date_check = ['REMOTE_ADDR', 'HTTP_REFERER']
    date_get = []
    for d in date_check:
        val = get_meta(d, request)
        date_get.append(val)
    print('\n\nTest')
    print(date_get)
    print('\n\n')
    date = StatiscticsHit(ip_client=date_get[0], link_client=date_get[1], date_client=datetime.now())
    date.save()
    return render(request, 'pageresume/index.html', {})


def statistics_hits(request):
    dates = []
    for date in StatiscticsHit.objects.all():
        dates.append((date.ip_client, date.link_client, date.date_client))
    return render(request, 'pageresume/statistics_hits.html', {'statistics': dates})



def get_meta(date, request):
    try:
        values = request.META[date]
        print(values)
        return (values)
    except:
        return 'unknown'
import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    data =[]
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        writer = csv.reader(csvfile)
        next(writer)
        for item in writer:
            data.append({'Name': item[1], 'Street': item[4], 'District':item[6]})
    paginator = Paginator(data, 10) 
    page = paginator.get_page(page_number)
    bus_stations = paginator.page(page_number).object_list
    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

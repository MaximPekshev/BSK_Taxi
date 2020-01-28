from django.shortcuts import render
from django.http import HttpResponse
from .models import Driver
from .models import Working_day


def show_index(request):

	drivers = Driver.objects.all()

	context = {

		'drivers':drivers,

	}

	return render(request, 'baseapp/base.html', context)

def show_driver(request, slug):

	driver = Driver.objects.get(slug = slug)

	working_days = Working_day.objects.filter(driver = driver).order_by("date")


	context = {

		'working_days': working_days, 'driver': driver,

	}

	return render(request, 'baseapp/driver.html', context)	
	
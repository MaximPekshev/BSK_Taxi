from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from .models import Working_day
from .forms import NewDriverForm


def show_index(request):

	if request.user.is_authenticated:

		drivers = Driver.objects.all()

		context = {

			'drivers':drivers,

		}

		return render(request, 'baseapp/base.html', context)

	else:

		return render(request, 'authapp/login.html')


def show_driver(request, slug):

	driver = Driver.objects.get(slug = slug)

	working_days = Working_day.objects.filter(driver = driver).order_by("date")


	context = {

		'working_days': working_days, 'driver': driver,

	}

	return render(request, 'baseapp/driver.html', context)	

def driver_add_new(request):
		
	if request.method == 'POST':

		dr_form = NewDriverForm(request.POST)

		if dr_form.is_valid():

			first_name 			= dr_form.cleaned_data['first_name']
			last_name 			= dr_form.cleaned_data['last_name']
			third_name 			= dr_form.cleaned_data['third_name']
			driver_license 		= dr_form.cleaned_data['driver_license']
			car_model 			= dr_form.cleaned_data['car_model']
			car_number 			= dr_form.cleaned_data['car_number']
			rate 				= dr_form.cleaned_data['rate']

			new_driver = Driver(
				first_name=first_name, second_name=last_name, 
				third_name=third_name,
				driver_license=driver_license,
				car_number=car_number, car_model=car_model,
				rate=rate, debt=0,
				)
			new_driver.save()

			return redirect('show_index')
	else:

		return redirect('show_index')

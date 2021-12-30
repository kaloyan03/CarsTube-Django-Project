from django.shortcuts import render, redirect
from cars_tube.cars.models import Car
from cars_tube.cars.forms import carForm
# Create your views here.


def list_cars(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'list_cars.html', context)


def add_car(request):
    if request.method == 'GET':
        form = carForm()
        context = {
            'form': form
        }

        return render(request, 'add_car.html', context)

    else:
        form = carForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('list cars')


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'GET':
        form = carForm(initial=car.__dict__)
        context = {
            'form': form,
            'car': car,
        }

        return render(request, 'edit_car.html', context)

    else:
        form = carForm(request.POST, instance=car)

        if form.is_valid():
            form.save()

            return redirect('car details', car.id)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'car': car,
        }

        return render(request, 'delete_car.html', context)

    else:
        car.delete()
        return redirect('list cars')


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car,
    }

    return render(request, 'car_details.html', context)
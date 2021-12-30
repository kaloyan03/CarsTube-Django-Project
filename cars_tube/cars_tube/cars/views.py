from django.shortcuts import render

# Create your views here.


def list_cars(request):
    return render(request, 'list_cars.html')


def create_car(request):
    pass


def edit_car(request):
    pass


def delete_car(request):
    pass
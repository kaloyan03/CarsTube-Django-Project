from django.urls import path

from cars_tube.cars.views import list_cars, edit_car, add_car, delete_car, car_details

urlpatterns = [
    path('', list_cars, name="list cars"),
    path('edit/<int:pk>', edit_car, name="edit car"),
    path('add-car/', add_car, name="add car"),
    path('delete/<int:pk>', delete_car, name="delete car"),
    path('details/<int:pk>', car_details, name="car details"),
]

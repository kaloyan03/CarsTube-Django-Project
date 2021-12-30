from django.urls import path

from cars_tube.cars.views import list_cars, edit_car, create_car, delete_car

urlpatterns = [
    path('', list_cars, name="list cars"),
    path('edit/<int:pk>', edit_car, name="edit car"),
    path('create/', create_car, name="create car"),
    path('delete/<int:pk>', delete_car, name="list cars"),
]

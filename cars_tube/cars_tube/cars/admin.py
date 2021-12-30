from django.contrib import admin
from cars_tube.cars.models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','brand', 'model', 'price', 'fuel')


admin.site.register(Car, CarAdmin)
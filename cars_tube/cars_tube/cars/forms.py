from django import forms
from cars_tube.cars.models import Car
from cars_tube.core.forms import BootstrapFormMixin


class carForm(BootstrapFormMixin ,forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
from django.urls import path

from cars_tube.common.views import landing_page

urlpatterns = [
    path('', landing_page, name="landing page"),
]

from django.urls import path
from cars_tube.cars_auth.views import sign_in, sign_up, sign_out

urlpatterns = [
    path('sign-in/', sign_in, name='sign in'),
    path('sign-up/', sign_up, name='sign up'),
    path('sign-out/', sign_out, name='sign out'),
]

import cars_tube.cars_auth.signals
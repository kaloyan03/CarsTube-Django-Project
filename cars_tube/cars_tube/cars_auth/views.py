from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from cars_tube.cars_auth.forms import SignInForm


def sign_up(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form,
        }

        return render(request, 'auth/sign_up.html', context)

    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sign in')

        else:
            print(form.errors)



def sign_in(request):
    if request.method == 'GET':
        form = SignInForm()
        context = {
            'form': form,
        }

        return render(request, 'auth/sign_in.html', context)

    else:
        form = SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password= password,
            )

            if user is not None:
                login(request, user)



def sign_out(request):
    pass
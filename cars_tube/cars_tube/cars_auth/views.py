from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from cars_tube.cars_auth.forms import SignInForm, ProfileForm


def sign_up(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('sign in')

    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'auth/sign_up.html', context)






def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')

    else:
        form = SignInForm()
    context = {
        'form': form,
    }

    return render(request, 'auth/sign_in.html', context)



def sign_out(request):
    logout(request)
    return redirect('landing page')
from django.shortcuts import render, redirect


# Create your views here.
def singup_profile(request):
    context = {

    }
    return render(request, 'accounts/register-page.html', context)


def singout_profile(request):
    return redirect('index')


def signin_profile(request):
    context = {

    }
    return render(request, 'accounts/login-page.html', context)


def details_profile(request, pk):
    context = {

    }

    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    context = {

    }
    return render(request, 'accounts/profile-edit-page.html', context)


def delete_profile(request, pk):
    context = {

    }
    return render(request, 'accounts/profile-delete-page.html', context)


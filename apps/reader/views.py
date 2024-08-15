from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    # unbound or pre-submit state
    error_message = None 
    form = AuthenticationForm()

    if request.method == 'POST':
        # bound or post-submit state
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate reader
            reader = authenticate(
                username=username,
                password=password,
            )
            if reader is not None:
                login(request, reader)
                return redirect('reader-urls:reader-profile')
        else:
            error_message = 'Sorry, something went wrong, Try again'

    context = {"form": form, "error_message": error_message}
    return render(request, 'login.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')
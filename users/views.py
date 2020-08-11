from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import * 


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Check if the form is valid after submission
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Redirect back to login page once registered
            messages.success(request, f'Your account has been created! You are \
                    now able to login.') 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # Saving form data once checked valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # Redirect back to ile page once info updated 
            messages.success(request, f'Your account has been updated!')
            # Prevent form re-submission msg from browser
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
            }
    return render(request, 'users/profile.html', context)

# Notes for myself
# messages methods: debug, info, success, warning, error


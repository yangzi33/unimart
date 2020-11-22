from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import * 

# For REST Api
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import * 


# Rest Views ################

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serailizer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


#############################


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
    return render(request, 'account/register.html', {'form': form})


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


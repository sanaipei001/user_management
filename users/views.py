from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm, UserUpdateForm, PasswordChangeForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user).generate_verification_token()
            login(request, user)
            messages.success(request, 'Registration successful! Please verify your account.')
            return redirect('verify')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def verify(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        profile = UserProfile.objects.filter(verification_token=token).first()
        if profile:
            profile.is_verified = True
            profile.verification_token = ''
            profile.save()
            messages.success(request, 'Account verified!')
            return redirect('profile')
        messages.error(request, 'Invalid token.')
    return render(request, 'users/verify.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'users/logout.html')
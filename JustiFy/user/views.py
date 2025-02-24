from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomAuthenticationForm, EditUserForm, EditProfileForm
from .models import CustomUser, Profile
from .tokens import generate_verification_token, verify_verification_token

from django.contrib.auth.decorators import login_required
from crime.models import SharedPost

@login_required
def shared_posts(request):
    shared = SharedPost.objects.filter(user=request.user).order_by('-shared_at')
    return render(request, "user/shared_posts.html", {'shared_posts': shared})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set role based on admin email list from settings.
            admin_emails = getattr(settings, "ADMIN_EMAILS", [])
            user.role = "admin" if user.email in admin_emails else "normal"
            user.is_verified = False  # New users need to verify their email.
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("user:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "user/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("user:profile")
    else:
        form = CustomAuthenticationForm()
    return render(request, "user/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("user:login")

@login_required
def profile(request):
    return render(request, "user/profile.html", {"user": request.user})

@login_required
def send_verification_email(request):
    user = request.user
    if user.is_verified:
        messages.info(request, "Your email is already verified.")
        return redirect("user:profile")
    token = generate_verification_token(user)
    verification_url = request.build_absolute_uri(
        reverse("user:verify_email", kwargs={"token": token})
    )
    subject = "Verify your email"
    message = f"Hi, please click the following link to verify your email:\n{verification_url}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    # Render the dedicated "send verification email" page.
    return render(request, "user/send_verification_email.html")

def verify_email(request, token):
    user_id = verify_verification_token(token)
    if user_id:
        user = get_object_or_404(CustomUser, pk=user_id)
        user.is_verified = True
        user.save()
        messages.success(request, "Your email has been verified!")
        return render(request, "user/email_verified.html")
    else:
        messages.error(request, "Verification link is invalid or expired.")
        return redirect("user:login")

@login_required
def edit_profile(request):
    user = request.user
    # Fallback for missing profile
    profile, _ = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("user:profile")
    else:
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)

    return render(request, "user/edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })
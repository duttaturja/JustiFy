from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(required=True, max_length=20)

    class Meta:
        model = CustomUser
        fields = ("email", "phone",)

class CustomAuthenticationForm(AuthenticationForm):
    # Uses the custom user model's email as the username field.
    pass

class EditUserForm(forms.ModelForm):
    # Assuming you want to allow editing of first and last names (if added) and phone.
    first_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=False, max_length=30)
    phone = forms.CharField(required=True, max_length=20)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "phone",)

class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 4}))
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ("bio", "profile_image",)

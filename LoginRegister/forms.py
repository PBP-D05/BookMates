from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User model
from .models import UserProfile
from MengelolaBuku.models import Pengguna

class RegistrationForm(UserCreationForm):
    is_teacher = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User  # Use the built-in User model
        fields = ["username", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        # Create a related Pengguna instance
        Pengguna.objects.create(user=user, isGuru=self.cleaned_data['is_teacher'], point=0)
        return user
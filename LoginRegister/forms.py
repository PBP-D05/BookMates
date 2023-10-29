from django import forms
from LoginRegister.models import Pengguna
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    is_teacher = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Pengguna
        fields = ["username", "password1", "password2", "is_teacher"]
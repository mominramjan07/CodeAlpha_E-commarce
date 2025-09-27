from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# ✅ Checkout Form
class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)


# ✅ Signup Form (User Registration)
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

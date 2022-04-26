from django import forms
from .models import InsuranceModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email Address', required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput()}
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = InsuranceModel
        fields = ['prod_info', 'age', 'height', 'weight', 'bmi', 'employee', 'insurance', 'insurancehist1', 'insurancehist2', 'family_his', 'medical_his']
        #fields = '__all__'
        labels = {'prod_info': 'Product Information','insurancehist1': 'Insurance History 1', 'insurancehist2': 'Insurance History 2', 'family_his': 'Family History','medical_his': 'Medical History'}
        widgets = {'prod_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Product Info"}),
                   'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Age"}),
                   'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Height"}),
                   'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Weight"}),
                   'bmi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Bmi"}),
                   'employee': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Employee"}),
                   'insurance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insurance"}),
                   'insurancehist1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insurance History 1"}),
                   'insurancehist2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insurance History 2"}),
                   'family_his': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Family History"}),
                   'medical_his': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Medical History"}),

                   }
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


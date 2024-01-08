from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

# Form for the register page
class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }
        widget = {
            'email': forms.EmailInput(attrs={
                'class': 'form-input form-email',
                'id': 'form-email',
                'placeholder': 'Your email...'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-input form-first-name',
                'id': 'form-first-name',
                'placeholder': 'Your first name...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input form-last-name',
                'id': 'form-last-name',
                'placeholder': 'Your last name...'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-input form-password-one',
                'id': 'form-password-one',
                'placeholder': 'Your new password...'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-input form-password-two',
                'id': 'form-password-two',
                'placeholder': 'Repeat new password...'
            }),            
        }

# Form for the login page
class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Password'
        }
        widget = {
            'email': forms.EmailInput(attrs={
                'class': 'form-input form-email',
                'id': 'form-email',
                'placeholder': 'Your email...'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-input form-password',
                'id': 'form-password',
                'placeholder': 'Your password...'
            }), 
        }

# Form for user change form
class DetailChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
        widget = {
            'email': forms.EmailInput(attrs={
                'class': 'form-input form-email',
                'id': 'form-email',
                'placeholder': 'Your email...'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-input form-first-name',
                'id': 'form-first-name',
                'placeholder': 'Your first name...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input form-last-name',
                'id': 'form-last-name',
                'placeholder': 'Your last name...'
            })           
        }

# Form for the login page
class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Password'
        }
        widget = {
            'email': forms.EmailInput(attrs={
                'class': 'form-input form-email',
                'id': 'form-email',
                'placeholder': 'Your email...'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-input form-password',
                'id': 'form-password',
                'placeholder': 'Your password...'
            }), 
        }

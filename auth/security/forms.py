from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class UserLoginForm(UserCreationForm):
#     password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput, help_text="Enter the same password as above, for verification.")
#     full_name = forms.CharField(max_length=100)
#     class Meta:
#         model = User
#         fields = ['full_name', 'email']
#         # labels = {'email': 'Your Email', 'password2': '', 'full_name': 'Your Name'}
#         # error_messages = {
#         #     'email':{'required': 'Email is required.'},
#         # }
#         # widgets = {
#         #     'full_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#         #     'email': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#         #     'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
#         #     'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
#         # }
#         # def clean_email(self):
#         #     email = self.cleaned_data.get('email')
#         #     if ('@' and ".com") not in email:
#         #         raise forms.ValidationError("Please enter a valid email")
            
#         #     return email 
from django import forms
from app_password_auth.models import EndUserProfileInfo
from django.contrib.auth.models import User

class CustomUserForm(forms.ModelForm):
    class Meta():
        # Never use () to call EndUserProfileInfo
        model = EndUserProfileInfo
        # fields = '__all__'
        fields = ('end_user_site','end_user_dp')



class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email',)

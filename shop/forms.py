from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '👤 نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '👤 نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' 📧 ایمیل خود را وارد کنید'})
    )
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '🪪 نام کاربری را وارد کنید'})
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '🔑 رمز بالای ۸ کاراکتر را وارد '})
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '🔑 دوباره رمز خود را وارد '})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UpdateUserForm(UserChangeForm):
    password=None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '👤 نام خود را وارد کنید'},),
        required=False,
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '👤 نام خانوادگی خود را وارد کنید'}),
        required=False,
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' 📧 ایمیل خود را وارد کنید'}),
        required=False,
    )
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '🪪 نام کاربری را وارد کنید'}),
        required=False,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class UpdatePassswordForm(SetPasswordForm):


    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '🔑 رمز بالای ۸ کاراکتر را وارد '})
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '🔑 دوباره رمز خود را وارد '})
    )
    class Meta:
        model = User
        fields = ('new_password1','new_password2')


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(    
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تماس خود را وارد کنید'})
    )
    address1 = forms.CharField(     
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'})
    )
    address2 = forms.CharField(     
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'})
    )
    city = forms.CharField(  
          label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'})
    )
    state = forms.CharField(  
            label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'منطقه'})
   )
    zipcode = forms.CharField(     
         label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'کدپستی'})
   )
    country = forms.CharField(       
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'})
   )

    class Meta:
        model = Profile
        fields = ['phone','address1','address2','city','state','zipcode','country']

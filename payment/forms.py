from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    [] = forms.CharField(    
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '  نام خود را وارد کنید'})
    )
    [] = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' 📧 ایمیل خود را وارد کنید'}),
        required=True,
    )
    [] = forms.CharField(     
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'})
    )
    []= forms.CharField(     
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'})
    )
    [] = forms.CharField(  
          label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'})
    )
    [] = forms.CharField(  
            label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'منطقه'})
   )
    [] = forms.CharField(     
         label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'کدپستی'})
   )
    [] = forms.CharField(       
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'})
   )
    class Meta:
        fields = [
                'shipping_full_name',
                'shipping_email',
                'shipping_address1',
                'shipping_address2' ,
                'shipping_city',
                'shipping_state',
                'shipping_zipcode',
                'shipping_country'
                       
        ]
        exlcude = ['user',]
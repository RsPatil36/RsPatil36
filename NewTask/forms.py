from django import forms

# class UserRegisterForm(forms.Form):
#     Name = forms.CharField(max_length=64)
#     URL = forms.URLField(max_length=100)
#     Phone_Number = forms.CharField(max_length=10)
#
class Check_Name(forms.Form):
    Name = forms.CharField(max_length=64)

    # class Meta:
    #     model = User
    #     fields = ['username','email','password1','password2']
from .models import Data_saving_db

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model= Data_saving_db
        fields= ["Name", "URL", "Phone_Number"]

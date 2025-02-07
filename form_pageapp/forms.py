from django import forms
from form_pageapp.models import RegistrationUser


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices=RegistrationUser.GENDER_CHOICES,widget=forms.RadioSelect)

    class Meta:
        model = RegistrationUser
        fields = ['first_name','last_name','email','phone_number','gender']
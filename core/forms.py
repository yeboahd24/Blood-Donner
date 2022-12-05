from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import User, Donor
from captcha.fields import CaptchaField


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "captcha")

        


class DonerForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
        exclude = ("user", "last_donation_date",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        # self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        # self.fields["contact_number"].widget.attrs["placeholder"] = "Contact Number"
        # self.fields["location"].widget.attrs["placeholder"] = "Location"
        # self.fields["blood_group"].widget.attrs["placeholder"] = "Blood Group"
        # self.fields["date_of_birth"].widget.attrs["placeholder"] = "Date of Birth"
        # hide user field
        # self.fields["user"].widget = forms.HiddenInput()


        

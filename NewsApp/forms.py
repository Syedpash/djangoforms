from django import forms
from .models import RegistrationData

class RegistrationForm(forms.Form):
    # django form with there attrinutes
    username = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'Username'
                                }))
    password = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'password'
                                }))
    email = forms.CharField(max_length=100,
                                widget=forms.EmailInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'email'
                                }))
    phone = forms.CharField(max_length=100,
                                widget=forms.NumberInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'phone'
                                }))

# forms using models
class RegistrationModel(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields =[
            "username",
            "password",
            "email",
            "phone"
        ]
        # widgets in model form
        widgets = {
            'username': forms.TextInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'Username'
                                }),
            'password': forms.TextInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'password'
                                }),
            'email': forms.EmailInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'email'
                                }),
            'phone': forms.NumberInput(attrs= {
                                    'class':'form-control',
                                    'placeholder':'phone'
                                })
        }
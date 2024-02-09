from django import forms
from .models import AuthUser

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')

        # Check if all fields are empty
        if not (username or password or email):
            raise forms.ValidationError("Please provide at least one field.")

        return cleaned_data
    
    
    #no finish I am chinees 
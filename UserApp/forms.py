from django import forms
from UserApp.models import User

class registrationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ["username","password","email"]
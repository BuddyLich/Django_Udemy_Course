from django import forms
from appTwo.models import User


class NewUserForm(forms.ModelForm):
    # custom field here if custom validation required
    class Meta:
        model = User
        fields = "__all__"

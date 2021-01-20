from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Remember not to use the same name with UserCreationForm
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].laberl = 'Display Name'
        self.fields['email'].laberl = 'Email Address'
        # customize the label of certain fields

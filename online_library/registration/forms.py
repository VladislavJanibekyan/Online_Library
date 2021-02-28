from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreate(UserCreationForm):
            class Meta:
                model = User
                fields=['username', 'password1', 'password2', 'email']
                help_texts = {'username': None, 'password1': (""), 'password2': (""),}

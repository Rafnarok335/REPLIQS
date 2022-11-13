from django.contrib.auth.forms import UserCreationForm
from Company.models import User
#This is a customized user creation form that inherits from the UserCreationForm class
# I am using it to add a field for email i can also add other field here. But i kept it minimal.
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
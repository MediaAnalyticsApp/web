from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self). __init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control input'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) < 3:
            raise forms.ValidationError('username не должно быть короче 3 символов!')

        return data


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) < 3:
            raise forms.ValidationError('username не должно быть короче 3 символов!')

        return data

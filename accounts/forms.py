from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update( {'class': 'form-control'} )

class UsernamePasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Username")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            return username
        except User.DoesNotExist:
            raise forms.ValidationError("This username does not exist.")

class CustomPasswordResetForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        label="New Password",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")

        if len(new_password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if self.user:
            try:
                validate_password(new_password, self.user)
            except ValidationError as e:
                raise ValidationError(e.messages)

        return new_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise ValidationError("Passwords do not match.")

        return cleaned_data
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from home.models import ContactForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ContactForm(ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(max_length=50)

    class Meta:
        model = ContactForm
        fields = (
        'name',
        'email',
        'phone',
        'message'
        )

    def save(self, commit=True):
        form = super(ContactForm, self).save(commit=False)
        form.name = self.cleaned_data['name']
        form.email = self.cleaned_data['email']
        form.phone = self.cleaned_data['phone']
        form.message = self.cleaned_data['message']
        if commit:
            form.save()

        return form

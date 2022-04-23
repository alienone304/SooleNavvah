from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    '''form for creating a user'''

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'uk-input fHarmattan','placeholder':'شماره تلفن مثال 9141234567','id':'username','onblur':'checkLength(this)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fHarmattan redC-text','placeholder':'رمز عبور'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fHarmattan redC-text','placeholder':'تکرار رمز عبور'
        }))

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username','email',
                  'name','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'شماره همراه','id':'username','onblur':'checkLength(this)'},),
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'نام و نام خانوادگی'},),
        }


class TypesForm(forms.Form):

    commonusers = forms.BooleanField(required=False)

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class UserLoginForm(AuthenticationForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'uk-input fYekan redC-text','placeholder':'','id':'',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fYekan redC-text','placeholder':''
        }
))
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

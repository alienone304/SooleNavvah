from django import forms
from django.core import validators
from comment.models import CommentModel, FamousCustomerModel

class CommentForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = CommentModel
        fields = ('project_name','project','comment','person_name','picture')
        widgets = {
            'project_name': forms.TextInput(attrs={'class':'uk-input fYekan redC-text','placeholder':''},),
            'person_name': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'project': forms.Select(attrs={'class':'uk-select fYekan'},),
            'picture': forms.FileInput(attrs={'class':'uk-button fYekan'},),
            'comment': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'4','placeholder':'دیدگاه مشتری را در این قسمت وارد کنید.'},),

        }


class FamousCustomeForm(forms.ModelForm):
    class Meta():
        model = FamousCustomerModel
        fields = ('picture','description',)
        widgets = {
            'picture': forms.FileInput(attrs={'class':'uk-button',},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'2','placeholder':'توضیحات'},),
        }

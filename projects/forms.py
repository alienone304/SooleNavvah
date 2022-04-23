from django import forms
from django.core import validators
from projects.models import ProjectsModel, ProjectPictureModel

class ProjectsForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = ProjectsModel
        fields = ('project_name','length','width','height','use_type','roof_type','date_of_project',
                'customer_name','is_local','description','contact_info','address',)
        widgets = {
            'project_name': forms.TextInput(attrs={'class':'uk-input fYekan redC-text','placeholder':''},),
            'length': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'width': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'height': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'use_type': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'roof_type': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'date_of_project': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'customer_name': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'is_local': forms.CheckboxInput(attrs={'class':'uk-checkbox fYekan '},),

            'address': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'3','placeholder':'محل نصب سالن'},),
            'contact_info': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'3','placeholder':'در صورت نیاز اطلاعات تماس سالن اعم از آدرس سایت و شماره تماس و .. را در این قسمت وارد کنید'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'3','placeholder':'در صورت نیاز توضیحات دیگر مانند وجود بچه سوله یا چند طبقه بودن یا .. را در این قسمت وارد کنید.'},),

        }



class ProjectPictureForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = ProjectPictureModel
        fields = ('picture','description')
        widgets = {
            'picture': forms.FileInput(attrs={},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'2','placeholder':'کپشن عکس'},),
        }


class ProjectPictureUpdateForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = ProjectPictureModel
        fields = ('picture','description')
        widgets = {
            'picture': forms.FileInput(attrs={},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'2','placeholder':'کپشن عکس'},),
        }

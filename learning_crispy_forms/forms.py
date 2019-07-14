from django import forms
# from django.core import validators
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


States=(
    ('','Choose..'),
    ('MP','Madhya Pradesh'),
    ('KA','Karnataka'),
    ('UP','Uttar Pradesh')
)

class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter the name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    verify_email=forms.EmailField(label="Enter ur email again",widget=forms.EmailInput(attrs={'placeholder':'Enter the email again'}))
    address1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Kumta'}))
    city=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Bangalore'}))
    state=forms.ChoiceField(choices=States)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.layout=Layout(
            'name',
            Row(
                Column('email',css_class='form-group col-md-6 mb-0'),
                Column('verify_email',css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address1',css_class='form-group col-md-6 mb-0'),
                Column('city', css_class='form-group col-md-4 mb-0'),
                Column('state', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'

            )
        )






from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from django.forms import ModelForm
from mailarep_app.models import Sender


class SenderModelForm(ModelForm):
    class Meta:
        model = Sender
        fields = ['name', 'street_address', 'city', 'state', 'zip_code',
                  'phone_number', 'email_address']

    def __init__(self, *args, **kwargs):
        super(SenderModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_action = 'new-sender'
        self.helper.form_id = 'new-sender'
        self.helper.form_class = 'blueForms'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name', placeholder="Sally Citizen"),
            Field('street_address', placeholder="123 State St."),
            Field('city', placeholder="Sunnyvale"),
            Field('state'),
            Field('zip_code', placeholder="12345"),
            Field('phone_number', placeholder="(123) 555-4567"),
            Field('email_address', placeholder="test@example.com"),
        )
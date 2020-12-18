from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from django.forms import ModelForm

from curry.apps.zvitae.models import Zvitae, CivilState, Address


class ZvitaeModelForm(BSModalModelForm):
    class Meta:
        model = Zvitae
        fields = ['title', 'description']


class ZvitaeForm(ModelForm):

    class Meta:
        model = Zvitae
        fields = ['title', 'description']


class CstateForm(forms.ModelForm):

    class Meta:
        model = CivilState
        fields = ['age', 'first_name', 'last_name', 'phone', 'linkedin', 'email', 'driving_licence']


class AddressForm(ModelForm):
    address2 = forms.CharField(required=False)

    class Meta:
        model = Address
        fields = ['number', 'address', 'address2', 'city', 'postal_code']

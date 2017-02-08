from django import forms
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Field
from django.core import validators
from restaurantes.models import Restaurantes
import requests
from django.forms import IntegerField, CharField, ChoiceField


class formAdd(forms.Form):
	
	id_restaurante = forms.CharField(widget=forms.HiddenInput(),required=False)
	
	nombre = forms.CharField(max_length=65,widget=forms.TextInput({'class': 'form-control', "placeholder": "Restaurante"}),required=True) #validaciones 
	cocina = forms.CharField(max_length=65,widget=forms.TextInput({'class': 'form-control', "placeholder": "Tipo de Cocina"}),required=True)
	ciudad = ChoiceField(
	choices=(
            ('Manhattan', "Manhattan (1-10)"),
            ('Brooklyn', "Brooklyn (11-20)"),
            ('Queens', "Queens (20-30)"),
            ('Staten Island', "Staten Island (30-40)"),
            ('Bronx', "Bronx (40-50)")
        ),
        widget=forms.RadioSelect,
        initial='Manhattan',
	)
	zipcode = forms.IntegerField()
	 
	def clean(self):

		self.is_valid()
		borough = self.cleaned_data.get('ciudad')
		code = self.cleaned_data.get('zipcode')
		if (borough == 'Manhattan' and 1 < code < 10) or (borough == 'Brooklyn' and 11 < code < 20) or \
			(borough == 'Queens' and 21 < code < 30) or (borough == 'Staten Island' and 31 < code < 40)\
			or (borough == 'Bronx' and 10450 < code < 10475):
			return self.cleaned_data
		raise forms.ValidationError('El codigo postal no corresponde con el barrio')
		
	def save(self):
		saveR=Restaurantes()
		return saveR.addRestaurant(self.cleaned_data)
	
	def update(self):
		updR=Restaurantes()
		return updR.modifyRestaurant(self.cleaned_data)

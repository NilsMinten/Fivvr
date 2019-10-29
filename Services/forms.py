from django import forms
from .models import Service


class CustomServiceCreationForm(Service):
    class Meta:
        model = Service
        fields = '__all__'


class CustomServiceEditnForm(Service):
    class Meta:
        model = Service
        fields = '__all__'

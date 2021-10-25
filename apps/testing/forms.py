from django import forms
from django.forms.forms import Form

class NameForm(forms.Form):
    """
    DETERMINA LA ESTRUCTRA DE LOS INPUT
    ADEMAS CON ESTO SE DETERMINA LA BASE DE LAS VALIDACIONES
    """
    your_name = forms.CharField(label='Nombre',max_length=5)
    your_lname = forms.CharField(label='Apellido',max_length=5)
    your_age = forms.IntegerField(label='Edad',max_value=10)
    your_birthday = forms.DateField(label='Fecha de nacimiento')
    your_datetime = forms.DateTimeField(label='Datetime')

    def second_str(self):
        form = 'hola'

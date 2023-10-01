import floppyforms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from django import forms

from .models import DeliveryConfig
from ..companies.models import Brand


class DeliveryConfigForm(forms.ModelForm):
    start_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y')
    )
    end_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y')
    )
    delivery_days = forms.MultipleChoiceField(
        choices=[
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo')
        ],
        widget=floppyforms.CheckboxSelectMultiple,
    )

    reminder_delivery_days = forms.MultipleChoiceField(
        choices=[
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo')
        ],
        widget=floppyforms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = DeliveryConfig
        fields = '__all__'
        optional_fields = ['reminder_delivery_days'],
        exclude = ['created_at', 'updated_at']

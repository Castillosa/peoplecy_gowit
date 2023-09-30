import floppyforms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from django import forms

from .models import DeliveryConfig


class DeliveryConfigForm(forms.ModelForm):
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
    )

    class Meta:
        model = DeliveryConfig
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

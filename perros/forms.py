from django import forms
from .models import Perro, Cruce

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ["nombre", "raza", "madre", "padre"]

class CruceForm(forms.ModelForm):
    class Meta:
        model = Cruce
        fields = ["fecha_insem"]
        widgets = {
            "fecha_insem": forms.DateInput(attrs={"type": "date"}),
        }

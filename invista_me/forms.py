from attr import field
from django.forms import ModelForm
from .models import Gasto, Investimento


class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'


class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

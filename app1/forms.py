from django import forms
from app1.models import Cliente, Carro, Sorteio

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        help_texts = {
        'parcelas': ('Insira um valor entre 36 e 180 meses.'),
        }
    
class CarroModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

class SorteioModelForm(forms.ModelForm):
    class Meta:
        model = Sorteio
        fields = '__all__'
        widgets = {
            'vencedor': forms.HiddenInput(),
        }
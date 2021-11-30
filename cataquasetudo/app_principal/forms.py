from django import forms

from app_principal.models import Contrato, Transporte

class TransporteCreateForm(forms.ModelForm):
    class Meta:
        model = Transporte
        
        fields = [
            'prestador',
            'veiculo',
            'capacidade',
            'moveis',
            'eletro',
            'metais',
            'alvenaria',
            'madeiramento',
            'troncos',
            'arbusto',
            'grama',
            'preco'
        ]
        exclude = [
            'codigo'
        ]

class ContratoCreateForm(forms.ModelForm):
    class Meta:
        model = Contrato
        
        fields = [
            'cliente',
            'transporte',
            'quantidade',
            'moveis',
            'eletro',
            'metais',
            'alvenaria',
            'madeiramento',
            'troncos',
            'arbusto',
            'grama'
        ]
        exclude = [
            'codigo'
        ]        
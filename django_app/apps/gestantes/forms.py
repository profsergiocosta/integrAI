from django import forms

from apps.gestantes.models import Gestante, Avaliacao
from django.utils.safestring import mark_safe



import random


## aqui irá entrar os modelos
# Funções para calcular as probabilidades
def calcular_probabilidade_asma(avaliacao):
    return round(random.uniform(0, 100), 2)

def calcular_probabilidade_obesidade(avaliacao):
    return round(random.uniform(0, 100), 2)

def calcular_probabilidade_carie(avaliacao):
    return round(random.uniform(0, 100), 2)


def calcular_probabilidade_alergia(avaliacao):
    return round(random.uniform(0, 100), 2)

def calcular_probabilidade_integralidade(avaliacao):
    return round(random.uniform(0, 100), 2)


class GestanteForms(forms.ModelForm):
    class Meta:
        model = Gestante
        
        exclude = ["usuario"]

        labels = {
            
            'data_cadastro': 'Data da inserção',
            'usuario': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'altura': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'inputmode': 'decimal',
                    'placeholder': 'Digite a altura (ex: 1,58)'
                }
            ),

            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
    

    
    def clean_altura(self):
        altura = self.cleaned_data['altura']
        if isinstance(altura, str):
            altura = altura.replace(',', '.')
        try:
            return float(altura)
        except ValueError:
            raise forms.ValidationError("Informe um número válido para a altura (ex: 1,65)")

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        exclude = [
            'gestante',
            'resultado_asma',
            'resultado_obesidade',
            'resultado_carie',
            'resultado_alergia',
            'resultado_integralidade_saude',
            'data_aplicacao'
        ]
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Chamada das funções simples (você define essas)
        instance.resultado_asma = {
            'probabilidade': calcular_probabilidade_asma(instance),
        }

        instance.resultado_obesidade = {
            'probabilidade': calcular_probabilidade_obesidade(instance),
        }

        instance.resultado_carie = {
            'probabilidade': calcular_probabilidade_carie(instance),
        }

        instance.resultado_alergia = {
            'probabilidade': calcular_probabilidade_alergia(instance),
        }

        instance.resultado_integralidade_saude = {
            'probabilidade': calcular_probabilidade_integralidade(instance),
        }

        if commit:
            instance.save()
        return instance
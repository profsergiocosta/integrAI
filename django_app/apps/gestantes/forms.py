from django import forms

from apps.gestantes.models import Gestante, Avaliacao
from django.utils.safestring import mark_safe

# Criar o widget personalizado
class CustomCheckboxInput(forms.CheckboxInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Renderiza o checkbox com o label após o campo
        checkbox_html = super().render(name, value, attrs, renderer)
        #print (checkbox_html, type(checkbox_html))
        #label = f'<label for="{attrs["id"]}">{self.attrs["label"]}</label>'
        label = '<label for="ola">ola</label>'
        return mark_safe(f'{checkbox_html}{label}')
        print (self.attrs)
        


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
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        exclude = ['gestante', 'probabilidade_asma', 'probabilidade_obesidade', 'probabilidade_carie']

 ## apagar depois  
class EmpresaForm(forms.Form):
    valor = forms.DecimalField(label="Valor da Empresa (em milhões)", min_value=0, required=True)
    costa = forms.ChoiceField(
        label="Localizada na Costa?", 
        choices=[("Sim", "Sim"), ("Não", "Não")],
        required=True
    )
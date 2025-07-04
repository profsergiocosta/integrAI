from django.db import models
from django import forms

from datetime import datetime

from django.utils import timezone

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.postgres.fields import JSONField  # Se estiver usando PostgreSQL

from django.templatetags.static import static
from datetime import date

class Gestante(models.Model):

    VULNERABILIDADE = [
        (True, 'Sim'),
        (False, 'Não'),
    ]

    nome = models.CharField(max_length=100)
    
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        blank=False,
        null=False
    )

    peso = models.PositiveIntegerField(
        verbose_name="Peso pré-gestacional (kg)",
        blank=False,
        null=False
    )
    altura = models.FloatField(
        verbose_name="Altura (m)",
        blank=False,
        null=False
    )

    vulnerabilidade_social = models.BooleanField(
        default=False, 
        choices=VULNERABILIDADE,
        blank=True,
        verbose_name='Com base nas suas visitas domiciliares, você considera essa gestante em condição de vulnerabilidade social?'
    )

    def foto_upload_path(instance, filename):
        return f'fotos/{instance.nome}_{instance.id}/{filename}'

    foto = models.ImageField(upload_to=foto_upload_path, blank=True)


    
    data_cadastro = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    @property
    def foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        return static('assets/imagens/gestante/silhueta.png')

    @property
    def imc(self):
        if self.altura > 0:
            return round(self.peso / (self.altura ** 2), 2)
        return None

    @property
    def imc_classificacao(self):
        imc = self.imc
        if imc is None:
            return "Altura ou peso inválidos"
        if imc < 18.5:
            return "Baixo peso"
        elif 18.5 <= imc <= 24.9:
            return "Adequado"
        else:
            return "Excesso de peso"
    
    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

    def clean(self):
        if self.peso < 30 or self.peso > 200:
            raise ValidationError("O peso deve estar entre 30 e 200 kg.")
        if self.idade < 10 or self.idade > 60:
            raise ValidationError("A idade deve estar entre 10 e 60 anos.")
        if self.altura < 1.0 or self.altura > 2.5:
            raise ValidationError("A altura deve estar entre 1.0 e 2.5 metros.")

    def __str__(self):
        return f"{self.nome} (ID: {self.id})"

    class Meta:
        ordering = ['-data_cadastro']
        verbose_name = "Gestante"
        verbose_name_plural = "Gestantes"


class Avaliacao(models.Model):

    PARTO_CHOICES = [
        ('Vaginal', 'Vaginal'),
        ('Cesáreo', 'Cesáreo'),
    ]


    gestante = models.ForeignKey(Gestante, on_delete=models.CASCADE, related_name='questionarios')
    
    data_aplicacao = models.DateTimeField(verbose_name="Data da Avaliação", default=timezone.now)


    peso_atual = models.FloatField(
        verbose_name="Peso atual:"
    )

    idade_gestacional = models.PositiveIntegerField(verbose_name="Idade Gestacional (em semanas)", null=True)

    consultas_prenatal = models.PositiveIntegerField(verbose_name="Quantidade de consultas pré-natal", null=True)

    corrimento_vaginal = models.BooleanField(
        default=False, 
        verbose_name='Durante a gestação, você apresentou ou apresenta corrimento vaginal frequente?'
    )

    periodontite_carie = models.BooleanField(
        default=False, 
        verbose_name='Você já teve cárie e/ou periodontite (inflamação na gengiva) diagnosticada nesta gestação?'
    )

    hipertensao_gestacao = models.BooleanField(
        default=False, 
        verbose_name='Você foi diagnosticada com hipertensão (pressão alta) nesta gestação?'
    )

    diabetes_gestacao = models.BooleanField(
        default=False, 
        verbose_name='Você foi diagnosticada com diabetes nesta gestação?'
    )

    estresse_gestacao = models.BooleanField(
        default=False,
        verbose_name='Você passou por algum estresse durante a gestação (violência, sobrecarga de trabalho)?'
    )

    historico_familiar_alergia = models.BooleanField(
        default=False,
        verbose_name='Algum membro da sua família (pai, mãe, irmãos) tem histórico de asma, rinite ou dermatite?'
    )

    consumo_bebidas_adocadas = models.BooleanField(
        default=False,
        verbose_name='Na última semana você consumiu refrigerante e outras bebidas industrializadas adoçadas artificialmente, como suco de caixinha, achocolatados, etc?'
    )

    consumo_ultraprocessados = models.BooleanField(
        default=False,
        verbose_name='Na última semana você consumiu alimentos ultraprocessados (ex.: sorvete, salgadinhos, salsicha, linguiça, presuntos, macarrão instantâneo, biscoitos recheados, etc)?'
    )

    consumo_alcool = models.BooleanField(
        default=False,
        verbose_name='Você consome/consumiu bebidas alcoólicas (cerveja, vinho, vodka, cachaça, etc) nesta gestação?'
    )

    fumante_gestacao = models.BooleanField(
        default=False,
        verbose_name='Você tinha o hábito de fumar ou fumou nesta gestação?'
    )



    resultado_asma = models.JSONField(null=True, blank=True)
    resultado_obesidade = models.JSONField(null=True, blank=True)
    resultado_carie = models.JSONField(null=True, blank=True)
    resultado_alergia = models.JSONField(null=True, blank=True)
    resultado_integralidade_saude = models.JSONField(null=True, blank=True)
    

    @property
    def ganho_peso(self):
        """Cálculo do ganho de peso durante a gestação"""
        if self.gestante and self.gestante.peso and self.peso_atual:
            return round(self.peso_atual - self.gestante.peso, 2)
        return None

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliações'
        ordering = ['gestante', 'data_aplicacao']  # Ordena por gestante e depois data

    def __str__(self):
        return f"Questionário de {self.gestante.nome} em {self.data_aplicacao.strftime('%d/%m/%Y')}"

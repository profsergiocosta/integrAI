from django.db import models

from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Gestante(models.Model):

    RESIDENCIA_CHOICES = [
        ('U', 'Urbana'),
        ('R', 'Rural'),
    ]

    OCUPACAO_CHEFE_CHOICES = [
        ('NQ', 'Mão de obra não qualificada (ex.: serviços gerais, agricultura, etc.)'),
        ('Q', 'Mão de obra qualificada (ex.: professor, técnico, etc.)'),
        ('D', 'Desempregada'),
    ]

    ESCOLARIDADE_CHOICES = [
        ('NS', 'Não estudou/sabe ler e escrever'),
        ('FI', 'Ensino fundamental incompleto'),
        ('MC', 'Ensino médio completo'),
        ('SC', 'Ensino superior completo'),
    ]

    nome = models.CharField(max_length=100)
    peso = models.PositiveIntegerField(verbose_name="Peso pré-gestacional (kg)")
    idade = models.PositiveIntegerField()
    
    def foto_upload_path(instance, filename):
        return f'fotos/{instance.nome}_{instance.id}/{filename}'

    foto = models.ImageField(upload_to=foto_upload_path, blank=True)
    residencia = models.CharField(
        max_length=1, 
        choices=RESIDENCIA_CHOICES, 
        default='U', 
        verbose_name="Em qual tipo de área está localizada a residência da gestante?"
    )
    ocupacao_chefe_familia = models.CharField(max_length=2, choices=OCUPACAO_CHEFE_CHOICES, verbose_name="Qual é a ocupação do chefe da família?", blank=True)
    nivel_escolaridade = models.CharField(max_length=2, choices=ESCOLARIDADE_CHOICES, verbose_name="Qual é o nível de escolaridade mais alto que você completou?", blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def clean(self):
        if self.peso < 30 or self.peso > 200:
            raise ValidationError("O peso deve estar entre 30 e 200 kg.")
        if self.idade < 10 or self.idade > 60:
            raise ValidationError("A idade deve estar entre 10 e 60 anos.")

    def __str__(self):
        return f"{self.nome} (Idade: {self.idade}, Residência: {self.get_residencia_display()})"

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
    data_aplicacao = models.DateTimeField(auto_now_add=True)
    peso_atual = models.FloatField(
        verbose_name="Peso atual:"
    )

    periodontite = models.BooleanField(
        default=False, 
        verbose_name='Você já teve periodontite (inflamação na gengiva) diagnosticada nesta gestação?'
    )
    carie_gestacao = models.BooleanField(
        default=False, 
        verbose_name='Você tem ou já teve cárie nesta gestação?'
    )
    orientacao_medica = models.BooleanField(
        default=False, 
        verbose_name='Você já teve orientação médica ou odontológica sobre cuidados durante a gestação?'
    )
    hipertensao_gestacao = models.BooleanField(
        default=False, 
        verbose_name='Você foi diagnosticada com hipertensão (pressão alta) nesta gestação?'
    )
    dificuldade_acesso = models.BooleanField(
        default=False, 
        verbose_name='Durante a gestação, você sentiu dificuldade em acessar atendimento médico ou exames necessários?'
    )

    tipo_parto = models.CharField(
        max_length=10,
        choices=PARTO_CHOICES,
        verbose_name='Você pretende ter o seu filho de parto vaginal ou cesáreo?',
        default='Vaginal'
    )


   # Novas colunas para probabilidades
    probabilidade_asma = models.FloatField(null=True, blank=True)
    probabilidade_obesidade = models.FloatField(null=True, blank=True)
    probabilidade_carie = models.FloatField(null=True, blank=True)


    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliação'  # Mantém o nome no singular no admin

    def __str__(self):
        return f"Questionário de {self.gestante.nome} em {self.data_aplicacao.strftime('%d/%m/%Y')}"

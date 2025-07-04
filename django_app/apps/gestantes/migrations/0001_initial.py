# Generated by Django 5.1.2 on 2025-04-30 11:21

import apps.gestantes.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('peso', models.PositiveIntegerField(verbose_name='Peso pré-gestacional (kg)')),
                ('altura', models.FloatField(verbose_name='Altura (m)')),
                ('vulnerabilidade_social', models.BooleanField(blank=True, choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Com base nas suas visitas domiciliares, você considera essa gestante em condição de vulnerabilidade social?')),
                ('foto', models.ImageField(blank=True, upload_to=apps.gestantes.models.Gestante.foto_upload_path)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gestante',
                'verbose_name_plural': 'Gestantes',
                'ordering': ['-data_cadastro'],
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_aplicacao', models.DateTimeField(auto_now_add=True)),
                ('peso_atual', models.FloatField(verbose_name='Peso atual:')),
                ('idade_gestacional', models.PositiveIntegerField(null=True, verbose_name='Idade Gestacional ou Trimestre da Gestação')),
                ('consultas_prenatal', models.PositiveIntegerField(null=True, verbose_name='Quantidade de consultas pré-natal')),
                ('periodontite', models.BooleanField(default=False, verbose_name='Você já teve periodontite (inflamação na gengiva) diagnosticada nesta gestação?')),
                ('carie_gestacao', models.BooleanField(default=False, verbose_name='Você tem ou já teve cárie nesta gestação?')),
                ('orientacao_medica', models.BooleanField(default=False, verbose_name='Você já teve orientação médica ou odontológica sobre cuidados durante a gestação?')),
                ('hipertensao_gestacao', models.BooleanField(default=False, verbose_name='Você foi diagnosticada com hipertensão (pressão alta) nesta gestação?')),
                ('dificuldade_acesso', models.BooleanField(default=False, verbose_name='Durante a gestação, você sentiu dificuldade em acessar atendimento médico ou exames necessários?')),
                ('tipo_parto', models.CharField(choices=[('Vaginal', 'Vaginal'), ('Cesáreo', 'Cesáreo')], default='Vaginal', max_length=10, verbose_name='Você pretende ter o seu filho de parto vaginal ou cesáreo?')),
                ('probabilidade_asma', models.FloatField(blank=True, null=True)),
                ('probabilidade_obesidade', models.FloatField(blank=True, null=True)),
                ('probabilidade_carie', models.FloatField(blank=True, null=True)),
                ('gestante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionarios', to='gestantes.gestante')),
            ],
            options={
                'verbose_name': 'Avaliacao',
                'verbose_name_plural': 'Avaliação',
            },
        ),
    ]

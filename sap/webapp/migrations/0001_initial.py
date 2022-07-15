# Generated by Django 4.0.5 on 2022-07-14 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alumnos', models.CharField(max_length=255)),
                ('telefono_alumnos', models.CharField(blank=True, max_length=12, null=True)),
                ('email_alumnos', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profesor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lecciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_lecciones', models.CharField(max_length=255)),
                ('horas', models.IntegerField()),
                ('temario', models.FileField(null=True, upload_to='temario/')),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('alumnos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.alumnos')),
            ],
        ),
    ]

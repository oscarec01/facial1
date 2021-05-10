# Generated by Django 3.1.7 on 2021-05-06 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de user')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('lastname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de Perfil')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

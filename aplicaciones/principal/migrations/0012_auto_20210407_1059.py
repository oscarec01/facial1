# Generated by Django 2.2.5 on 2021-04-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_auto_20210407_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='url_documento',
            field=models.ImageField(upload_to='images/doc/<bound method Field.value_to_string of <django.db.models.fields.IntegerField>>'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='url_selfi',
            field=models.ImageField(upload_to='images/selfie/<bound method Field.value_to_string of <django.db.models.fields.IntegerField>>'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-21 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0002_auto_20190521_1830'),
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='colaboradores.Colaborador'),
            preserve_default=False,
        ),
    ]

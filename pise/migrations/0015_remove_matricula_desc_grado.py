# Generated by Django 3.2.9 on 2022-08-05 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pise', '0014_auto_20220803_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='desc_grado',
        ),
    ]
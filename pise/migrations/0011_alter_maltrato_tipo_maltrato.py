# Generated by Django 3.2.9 on 2021-11-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pise', '0010_auto_20211112_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maltrato',
            name='tipo_maltrato',
            field=models.CharField(choices=[('Hacia Estudiantes', (('adulto', 'Adulto a Estudiantes'), ('estudiante', 'Estudiante a Estudiante'))), ('Hacia Funcionarios', (('alumno_docente', 'Alumno a Docente o Funcionarios'), ('apoderado', 'Apoderado a Docente o Funcionarios')))], default='estudiante', max_length=255, null=True),
        ),
    ]

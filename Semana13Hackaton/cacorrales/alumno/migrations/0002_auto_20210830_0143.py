# Generated by Django 3.2.6 on 2021-08-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='id_alumno',
            new_name='id_alum',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='id_curso',
            new_name='id_cur',
        ),
    ]

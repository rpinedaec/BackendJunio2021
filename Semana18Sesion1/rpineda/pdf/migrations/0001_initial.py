# Generated by Django 3.2.8 on 2021-10-15 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro', models.CharField(max_length=3)),
                ('tipo_almacen', models.CharField(max_length=50)),
                ('cod_material', models.CharField(max_length=9)),
                ('desc_material', models.CharField(max_length=500)),
                ('unidad', models.CharField(max_length=10)),
                ('saldo_actual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
            ],
        ),
    ]
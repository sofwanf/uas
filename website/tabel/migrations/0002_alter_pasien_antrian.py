# Generated by Django 4.1.3 on 2022-12-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasien',
            name='Antrian',
            field=models.CharField(max_length=10),
        ),
    ]

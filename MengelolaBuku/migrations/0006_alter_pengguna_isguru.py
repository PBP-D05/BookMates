# Generated by Django 4.2.5 on 2023-10-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MengelolaBuku', '0005_pengguna_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengguna',
            name='isGuru',
            field=models.BooleanField(default=True),
        ),
    ]

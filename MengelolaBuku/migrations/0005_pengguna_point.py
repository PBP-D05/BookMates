# Generated by Django 3.2.19 on 2023-10-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MengelolaBuku', '0004_buku_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengguna',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
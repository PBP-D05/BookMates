# Generated by Django 3.2.19 on 2023-10-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MengelolaBuku', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='num_of_rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.19 on 2023-12-09 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MengelolaBuku', '0009_merge_20231209_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengguna',
            name='banyakBintang',
        ),
        migrations.RemoveField(
            model_name='pengguna',
            name='banyakReview',
        ),
    ]
# Generated by Django 3.2.19 on 2023-12-20 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MengelolaBuku', '0010_auto_20231209_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MengelolaBuku.pengguna'),
        ),
    ]
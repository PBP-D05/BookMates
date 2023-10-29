# Generated by Django 3.2.19 on 2023-10-28 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MengelolaBuku', '0004_buku_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('point', models.IntegerField()),
                ('deadline', models.DateTimeField()),
                ('description', models.TextField()),
                ('reply', models.TextField()),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='MengelolaBuku.buku')),
            ],
        ),
    ]

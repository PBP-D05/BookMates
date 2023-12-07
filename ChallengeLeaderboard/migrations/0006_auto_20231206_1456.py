# Generated by Django 3.2.19 on 2023-12-06 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MengelolaBuku', '0008_auto_20231206_1349'),
        ('ChallengeLeaderboard', '0005_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MengelolaBuku.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MengelolaBuku.pengguna')),
            ],
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
# Generated by Django 3.2.19 on 2023-10-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChallengeLeaderboard', '0002_newreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='reply',
            field=models.ManyToManyField(blank=True, to='ChallengeLeaderboard.NewReply'),
        ),
    ]

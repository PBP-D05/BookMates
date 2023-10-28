# Generated by Django 4.2.6 on 2023-10-27 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('komunitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='community',
            name='title',
        ),
        migrations.AddField(
            model_name='community',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='name',
            field=models.CharField(default='anonymous', max_length=200),
        ),
        migrations.AddField(
            model_name='community',
            name='topic',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='komunitas.community'),
        ),
    ]

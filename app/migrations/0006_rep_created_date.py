# Generated by Django 4.0.4 on 2022-05-13 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_set_reps'),
    ]

    operations = [
        migrations.AddField(
            model_name='rep',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='nome',
            field=models.CharField(default='Pizza Sem Nome', max_length=100),
        ),
    ]
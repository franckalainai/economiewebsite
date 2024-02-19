# Generated by Django 3.2.14 on 2022-09-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0002_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='direction_generale',
        ),
        migrations.AlterField(
            model_name='direction',
            name='category',
            field=models.CharField(choices=[('Direction centrale', 'Direction centrale')], default='doem', max_length=300),
        ),
    ]

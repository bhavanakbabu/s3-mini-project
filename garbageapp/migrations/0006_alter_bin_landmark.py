# Generated by Django 5.1.1 on 2024-10-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbageapp', '0005_regcomp_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='landmark',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

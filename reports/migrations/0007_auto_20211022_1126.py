# Generated by Django 3.2.8 on 2021-10-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_reportage_reportsalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportage',
            name='average',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='reportsalary',
            name='average',
            field=models.CharField(max_length=7),
        ),
    ]

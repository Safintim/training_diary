# Generated by Django 3.1.2 on 2020-10-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20201013_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprogramm',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]

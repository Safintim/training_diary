# Generated by Django 3.1.2 on 2020-10-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20201013_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на демонстрацию'),
        ),
    ]

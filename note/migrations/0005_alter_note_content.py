# Generated by Django 3.2 on 2021-06-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20210603_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]

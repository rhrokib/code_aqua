# Generated by Django 3.2 on 2021-06-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
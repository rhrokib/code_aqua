# Generated by Django 3.2 on 2021-06-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.CharField(blank=True, choices=[('blue', 'Kinda Blue'), ('coral', 'Living Coral'), ('green', 'Pastel Green'), ('purple', 'Lavender'), ('white', 'Not So White')], default='white', max_length=30),
        ),
    ]

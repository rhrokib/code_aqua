# Generated by Django 3.2 on 2021-06-03 18:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('deposite', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='elec_bill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='food_budget',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='gas_bill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='house_rent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_bill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='water_bill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='total_budget',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.CreateModel(
            name='PerPersonMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30)),
                ('total_meals', models.IntegerField(default=0, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.person')),
            ],
        ),
        migrations.CreateModel(
            name='DailySpend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('total_daily_meals', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, null=True)),
                ('meal', models.ManyToManyField(to='dashboard.PerPersonMeal')),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='members',
            field=models.ManyToManyField(to='dashboard.Person'),
        ),
    ]

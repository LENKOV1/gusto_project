# Generated by Django 3.1.6 on 2021-02-18 17:23

from django.db import migrations, models
import django.db.models.deletion
import main_gusto.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('photo', models.ImageField(upload_to=main_gusto.models.Dish.get_file_name)),
                ('dish_order', models.IntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('desc', models.CharField(max_length=150, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_gusto.category')),
            ],
        ),
    ]

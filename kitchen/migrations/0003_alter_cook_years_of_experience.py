# Generated by Django 4.1.7 on 2023-03-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_alter_cook_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='years_of_experience',
            field=models.IntegerField(default=0),
        ),
    ]

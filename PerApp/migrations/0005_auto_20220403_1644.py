# Generated by Django 3.0.8 on 2022-04-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerApp', '0004_auto_20220403_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='roll_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
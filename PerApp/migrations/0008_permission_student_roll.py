# Generated by Django 3.0.8 on 2022-04-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerApp', '0007_auto_20220404_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='student_roll',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
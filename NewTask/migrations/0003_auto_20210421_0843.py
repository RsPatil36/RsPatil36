# Generated by Django 3.1 on 2021-04-21 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewTask', '0002_auto_20210421_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_saving_db',
            name='Phone_Number',
            field=models.CharField(max_length=10),
        ),
    ]

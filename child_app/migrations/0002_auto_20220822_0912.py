# Generated by Django 3.1.7 on 2022-08-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_bearers',
            name='eid',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]

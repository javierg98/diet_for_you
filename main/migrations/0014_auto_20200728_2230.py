# Generated by Django 3.0 on 2020-07-29 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200728_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_data',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.2 on 2023-04-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baham', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='model_id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 2.2 on 2019-08-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 2.0.7 on 2019-03-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0007_auto_20181027_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

# Generated by Django 2.0.7 on 2019-03-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_auto_20190318_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sub_total',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]

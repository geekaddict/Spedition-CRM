# Generated by Django 2.0.7 on 2019-03-13 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_remove_invoice_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='balance_due',
            field=models.FloatField(default=0.0),
        ),
    ]

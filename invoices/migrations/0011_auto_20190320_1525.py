# Generated by Django 2.0.7 on 2019-03-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0010_invoice_sub_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='sub_total',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]

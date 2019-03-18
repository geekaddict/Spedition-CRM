# Generated by Django 2.0.7 on 2019-03-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_auto_20190317_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='cgst_net',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='igst_net',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sgst_net',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

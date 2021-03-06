# Generated by Django 2.1 on 2018-08-21 06:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0002_job_job_status'),
        ('customers', '0003_auto_20180818_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField(default=1)),
                ('currency', models.CharField(choices=[('INR', 'INR'), ('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], default='INR', max_length=3)),
                ('rate', models.FloatField(default=1.0)),
                ('exchange_rate', models.FloatField(default=1.0)),
                ('tax_rate', models.FloatField(default=18.0)),
                ('total', models.FloatField(blank=True, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice')),
            ],
        ),
    ]

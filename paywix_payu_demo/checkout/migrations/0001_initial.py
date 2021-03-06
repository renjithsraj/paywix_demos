# Generated by Django 3.0.8 on 2020-07-26 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('txn_id', models.CharField(max_length=120, unique=True, verbose_name='transaction id')),
                ('txn_status', models.CharField(choices=[('NS', 'Not Started'), ('IN', 'Initiated'), ('MP', 'Money With PayUMoney'), ('UD', 'Under Dispute'), ('RF', 'Refunded'), ('PR', 'Partially Refunded'), ('BD', 'Bounced'), ('FD', 'Failed'), ('SP', 'Settlement in Process'), ('CP', 'Completed'), ('SIN', 'Server Side Initiated')], default='SIN', max_length=3, verbose_name='trabsaction status')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='amount')),
                ('request_data', models.TextField(blank=True, null=True, verbose_name='Requested Data')),
                ('requested_hash', models.TextField(blank=True, null=True, verbose_name='Requested Hash')),
                ('response_data', models.TextField(blank=True, null=True, verbose_name='Response Data')),
                ('reponse_hash', models.TextField(blank=True, null=True, verbose_name='Response Hash')),
                ('payumoney_id', models.CharField(editable=False, max_length=120, verbose_name='payuMoneyId')),
                ('transaction_mode', models.CharField(blank=True, max_length=2, null=True, verbose_name='Mode')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

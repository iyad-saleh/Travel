# Generated by Django 3.2.8 on 2022-09-09 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip', '0001_initial'),
        ('reservation', '0001_initial'),
        ('passport', '0002_passport_author'),
        ('customer', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subreservation',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subreservation',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='subreservation',
            name='passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='passport.passport'),
        ),
        migrations.AddField(
            model_name='subreservation',
            name='pay_coin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subpayCoin', to='coin.coin'),
        ),
        migrations.AddField(
            model_name='subreservation',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.reservation'),
        ),
        migrations.AddField(
            model_name='subreservation',
            name='sell_coin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsellCoin', to='coin.coin'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CustomerCompany', to='customer.customer'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='pay_coin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payCoin', to='coin.coin'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='sell_coin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sellCoin', to='coin.coin'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trip.trip'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendorCompany', to='customer.customer'),
        ),
    ]

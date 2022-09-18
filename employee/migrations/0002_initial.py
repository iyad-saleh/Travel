# Generated by Django 3.2.8 on 2022-09-09 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_initial'),
        ('company', '0001_initial'),
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeetype',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employeetype',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='employee',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
        migrations.AddField(
            model_name='employee',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ManyToManyField(related_name='EmployeeType', to='employee.EmployeeType'),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin.coin'),
        ),
    ]

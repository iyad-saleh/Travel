# Generated by Django 3.2.8 on 2022-07-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
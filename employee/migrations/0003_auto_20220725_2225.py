# Generated by Django 3.2.8 on 2022-07-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='employeetype',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='employeetype',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='employee',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
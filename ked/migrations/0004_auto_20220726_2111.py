# Generated by Django 3.2.8 on 2022-07-26 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20220726_2040'),
        ('ked', '0003_alter_journal_journal_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='journal',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='ked',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='ked',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='sub_account_cridt',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='sub_account_dept',
        ),
        migrations.AddField(
            model_name='journal',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='ked',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='journal',
            name='account_cridt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_cridt', to='account.account'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='account_dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_dept', to='account.account'),
        ),
    ]
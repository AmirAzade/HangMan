# Generated by Django 5.0.3 on 2024-04-20 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HangManApp', '0003_rename_user_member_rename_user_score_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='member',
            new_name='member_model',
        ),
    ]

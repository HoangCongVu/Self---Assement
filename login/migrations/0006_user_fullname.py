# Generated by Django 5.0.6 on 2024-05-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_user_classname_alter_user_mssv'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
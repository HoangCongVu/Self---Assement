# Generated by Django 5.0.6 on 2024-05-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_group_followed_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followed_user_id',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='following_user_id',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_delete_mpersona_alter_user_cvpersona_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]

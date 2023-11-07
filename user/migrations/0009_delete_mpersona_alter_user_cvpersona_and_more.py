# Generated by Django 4.2.6 on 2023-11-06 23:40

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mPersona', '0001_initial'),
        ('user', '0008_alter_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mPersona',
        ),
        migrations.AlterField(
            model_name='user',
            name='cvPersona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.mpersona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]

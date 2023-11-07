# Generated by Django 4.2.6 on 2023-11-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_delete_musuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='mUsuario',
            fields=[
                ('CvUser', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('CvPerson', models.CharField(max_length=20)),
                ('Login', models.CharField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=128)),
                ('FecIni', models.DateField()),
                ('FecFin', models.DateField()),
                ('EdoCta', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
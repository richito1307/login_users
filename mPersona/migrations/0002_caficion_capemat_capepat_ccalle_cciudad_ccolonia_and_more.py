# Generated by Django 4.2.6 on 2023-11-24 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mPersona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cAficion',
            fields=[
                ('CvAficion', models.AutoField(primary_key=True, serialize=False)),
                ('DsAficion', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cApeMat',
            fields=[
                ('CvApeMat', models.AutoField(primary_key=True, serialize=False)),
                ('DsApeMat', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cApePat',
            fields=[
                ('CvApePat', models.AutoField(primary_key=True, serialize=False)),
                ('DsApePat', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cCalle',
            fields=[
                ('CvCalle', models.AutoField(primary_key=True, serialize=False)),
                ('DsCalle', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cCiudad',
            fields=[
                ('CvCiudad', models.AutoField(primary_key=True, serialize=False)),
                ('DsCiudad', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cColonia',
            fields=[
                ('CvColonia', models.AutoField(primary_key=True, serialize=False)),
                ('DsColonia', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cMunicipio',
            fields=[
                ('CvMunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('DsMunicipio', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cNombre',
            fields=[
                ('CvNombre', models.AutoField(primary_key=True, serialize=False)),
                ('DsNombre', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mpersona',
            name='Genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('G', '39 tipos de geis')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='mpersona',
            name='TpPerson',
            field=models.CharField(choices=[('C', 'Cliente'), ('P', 'Proveedor'), ('E', 'Empleado')], default='N', max_length=1),
        ),
        migrations.CreateModel(
            name='mDireccion',
            fields=[
                ('CvDireccion', models.AutoField(primary_key=True, serialize=False)),
                ('Numero', models.IntegerField(blank=True, null=True)),
                ('CodPos', models.IntegerField(blank=True, null=True)),
                ('Calle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.ccalle')),
                ('Ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.cciudad')),
                ('Colonia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.ccolonia')),
                ('Municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.cmunicipio')),
            ],
        ),
        migrations.AddField(
            model_name='mpersona',
            name='Aficion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.caficion'),
        ),
        migrations.AlterField(
            model_name='mpersona',
            name='ApeMat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.capemat'),
        ),
        migrations.AlterField(
            model_name='mpersona',
            name='ApePat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.capepat'),
        ),
        migrations.AlterField(
            model_name='mpersona',
            name='Nombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mPersona.cnombre'),
        ),
    ]

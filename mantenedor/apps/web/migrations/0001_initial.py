# Generated by Django 3.1.3 on 2020-11-04 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('Rut', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('mensaje', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCurso', models.CharField(max_length=20)),
                ('modelaidad', models.CharField(max_length=20)),
                ('valor', models.IntegerField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.alumno')),
            ],
        ),
    ]

# Generated by Django 2.0 on 2019-03-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado')], max_length=10)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuscripcionUsuario',
            fields=[
                ('numero_id', models.AutoField(editable=False, max_length=9999, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=25)),
                ('f_nacimiento', models.DateField()),
                ('ciudad', models.CharField(max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='email',
            field=models.ManyToManyField(to='suscripcionapp.SuscripcionUsuario'),
        ),
    ]

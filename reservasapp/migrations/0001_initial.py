# Generated by Django 2.0 on 2019-03-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=255, verbose_name='Nombre contacto')),
                ('email', models.EmailField(max_length=254, verbose_name='Email contacto')),
                ('fecha_evento', models.DateField(verbose_name='Fecha Reserva')),
                ('hora_evento', models.TimeField(verbose_name='Hora Reserva')),
                ('numeros_invitados', models.CharField(max_length=25, verbose_name='Número Invitados')),
                ('telefono_invitado', models.CharField(max_length=25, verbose_name='Telefóno contacto')),
                ('mensaje_evento', models.TextField(verbose_name='Mensaje')),
                ('reserva_realizada', models.BooleanField(default=False, verbose_name='Realizada?')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'ordering': ['fecha_evento'],
            },
        ),
    ]
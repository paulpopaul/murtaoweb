# Generated by Django 2.0 on 2019-03-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('estado', models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado')], default='Publicado', max_length=12)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('imagen', models.ImageField(upload_to='')),
                ('numero_id', models.AutoField(max_length=9999, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
    ]

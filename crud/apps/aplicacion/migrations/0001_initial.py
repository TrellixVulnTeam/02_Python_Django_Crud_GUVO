# Generated by Django 2.2.3 on 2019-07-26 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.IntegerField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Region')),
            ],
        ),
    ]

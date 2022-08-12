# Generated by Django 4.0.5 on 2022-07-23 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comic_app', '0002_personaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('compania', models.CharField(blank=True, choices=[('Marvel', 'Marvel'), ('DC', 'DC Comics'), ('Dark Horse', 'Dark Horse'), ('IDW', 'IDW Publishing')], max_length=45, null=True)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=145)),
                ('descripcion', models.CharField(max_length=256)),
                ('interes', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroTarjeta', models.IntegerField()),
                ('creditoMax', models.FloatField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comic_app.cliente')),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comic_app.tarjeta')),
            ],
        ),
    ]

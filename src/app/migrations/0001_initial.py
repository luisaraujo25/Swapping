# Generated by Django 4.0.3 on 2022-04-03 20:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SwapRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('confirmation1', models.BooleanField()),
                ('confirmation2', models.BooleanField()),
                ('st2up', models.IntegerField()),
                ('st2class', models.IntegerField()),
                ('st1ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('ucID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uc')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('schedule', models.DateField(default=django.utils.timezone.now)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('ucID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uc')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=45),
        ),
        migrations.AlterField(
            model_name='uc',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
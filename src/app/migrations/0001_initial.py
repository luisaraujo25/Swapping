# Generated by Django 4.0.4 on 2022-06-09 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('code', models.CharField(max_length=12)),
                ('course', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ClassUC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed1', models.BooleanField(default=False)),
                ('confirmed2', models.BooleanField(default=False)),
                ('date', models.CharField(max_length=50)),
                ('token1', models.CharField(max_length=30, null=True)),
                ('token2', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekDay', models.CharField(max_length=50)),
                ('startTime', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('typeClass', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('up', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=45)),
                ('course', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentUC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('initials', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddConstraint(
            model_name='uc',
            constraint=models.UniqueConstraint(fields=('code',), name='codeUnique'),
        ),
        migrations.AddField(
            model_name='studentuc',
            name='cl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class'),
        ),
        migrations.AddField(
            model_name='studentuc',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AddField(
            model_name='studentuc',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uc'),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='classUC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classuc'),
        ),
        migrations.AddField(
            model_name='request',
            name='class1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='class1', to='app.class'),
        ),
        migrations.AddField(
            model_name='request',
            name='class2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='class2', to='app.class'),
        ),
        migrations.AddField(
            model_name='request',
            name='st1ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='request1', to='app.student'),
        ),
        migrations.AddField(
            model_name='request',
            name='st2ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='request2', to='app.student'),
        ),
        migrations.AddField(
            model_name='request',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uc'),
        ),
        migrations.AddField(
            model_name='classuc',
            name='cl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class'),
        ),
        migrations.AddField(
            model_name='classuc',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uc'),
        ),
        migrations.AddConstraint(
            model_name='class',
            constraint=models.UniqueConstraint(fields=('code',), name='classCodeUnique'),
        ),
        migrations.AlterUniqueTogether(
            name='studentuc',
            unique_together={('student', 'uc', 'cl')},
        ),
        migrations.AlterUniqueTogether(
            name='classuc',
            unique_together={('uc', 'cl')},
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-05 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128)),
                ('online', models.BooleanField(default=True)),
                ('last_checked', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Uptime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status_checker.Node')),
            ],
        ),
    ]

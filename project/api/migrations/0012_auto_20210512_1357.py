# Generated by Django 2.2 on 2021-05-12 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210512_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalroom',
            old_name='room_fk',
            new_name='subroom',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_fk',
        ),
        migrations.AddField(
            model_name='room',
            name='subroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='api.Room'),
        ),
    ]

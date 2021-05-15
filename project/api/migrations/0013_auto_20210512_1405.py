# Generated by Django 2.2 on 2021-05-12 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210512_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalroom',
            old_name='subroom',
            new_name='room_fk',
        ),
        migrations.RemoveField(
            model_name='room',
            name='subroom',
        ),
        migrations.AddField(
            model_name='room',
            name='room_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roomroom', to='api.Room'),
        ),
    ]
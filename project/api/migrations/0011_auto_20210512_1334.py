# Generated by Django 2.2 on 2021-05-12 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210423_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_room', to='api.Room'),
        ),
    ]

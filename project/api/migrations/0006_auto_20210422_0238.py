# Generated by Django 2.2 on 2021-04-22 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20210422_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Functionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('identification_number', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('institutional_email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('personal_email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('birth_date', models.DateField(null=True)),
                ('profession', models.TextField(blank=True, max_length=500, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='functionary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'functionary',
                'verbose_name_plural': 'functionarys',
                'ordering': ['-id'],
            },
        ),
        migrations.RenameModel(
            old_name='HistoricalEmployee',
            new_name='HistoricalFunctionary',
        ),
        migrations.AlterModelOptions(
            name='historicalfunctionary',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical functionary'},
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]

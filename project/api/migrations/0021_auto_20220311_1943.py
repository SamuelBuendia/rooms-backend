# Generated by Django 2.2 on 2022-03-12 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_evidence_historicalevidence'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacherevidence', to='api.Functionary'),
        ),
        migrations.AddField(
            model_name='historicalevidence',
            name='teacher',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.Functionary'),
        ),
    ]

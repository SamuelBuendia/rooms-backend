# Generated by Django 2.2 on 2021-04-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210422_0215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='description',
            new_name='profession',
        ),
        migrations.RenameField(
            model_name='historicalemployee',
            old_name='description',
            new_name='profession',
        ),
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='identification_number',
            field=models.CharField(default=1000000, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='institutional_email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='identification_number',
            field=models.CharField(db_index=True, default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='institutional_email',
            field=models.EmailField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='personal_email',
            field=models.EmailField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]

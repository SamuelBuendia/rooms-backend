# Generated by Django 2.2 on 2022-03-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20220301_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='guide_file',
            field=models.FileField(blank=True, db_column='file_url', null=True, upload_to='GuideFile/'),
        ),
        migrations.AlterField(
            model_name='historicalfolder',
            name='guide_file',
            field=models.TextField(blank=True, db_column='file_url', max_length=100, null=True),
        ),
    ]
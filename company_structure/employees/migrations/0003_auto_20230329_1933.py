# Generated by Django 3.2.18 on 2023-03-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20230329_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='department',
            name='surname',
        ),
        migrations.AddField(
            model_name='employee',
            name='father_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='surname',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]

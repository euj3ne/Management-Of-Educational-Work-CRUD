# Generated by Django 3.2.6 on 2023-12-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20231217_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='number_groupn',
        ),
        migrations.AddField(
            model_name='works',
            name='number_group',
            field=models.CharField(blank=True, choices=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='groups',
            name='data_teacher',
            field=models.CharField(blank=True, choices=[(1, '123123123 123 123'), (2, '123 123 123')], max_length=100),
        ),
    ]

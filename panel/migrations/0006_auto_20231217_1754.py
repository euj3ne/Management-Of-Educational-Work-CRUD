# Generated by Django 3.2.6 on 2023-12-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_alter_groups_data_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='data_teacher',
            field=models.CharField(blank=True, choices=[(1, '123123123 123 123')], max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='number_group',
            field=models.CharField(blank=True, choices=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='sex',
            field=models.CharField(blank=True, choices=[('MALE', 'Мужчина'), ('FEMALE', 'Женщина')], max_length=10, null=True),
        ),
    ]

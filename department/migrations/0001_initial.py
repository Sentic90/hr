# Generated by Django 3.1.5 on 2021-01-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Dname', models.CharField(max_length=250)),
                ('Mgr_start_date', models.CharField(max_length=250)),
                ('dnumber', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
    ]

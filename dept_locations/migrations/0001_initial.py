# Generated by Django 3.1.5 on 2021-01-11 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeptLocations',
            fields=[
                ('Dlocation', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('Dnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
            options={
                'verbose_name_plural': 'Depts Locations',
            },
        ),
    ]

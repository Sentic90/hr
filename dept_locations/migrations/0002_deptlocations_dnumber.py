# Generated by Django 3.1.5 on 2021-01-12 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_department_mgr_ssn'),
        ('dept_locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deptlocations',
            name='dnumber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
    ]
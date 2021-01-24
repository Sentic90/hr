# Generated by Django 3.1.4 on 2021-01-17 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Project', '0001_initial'),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WORKS_ON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hours', models.TimeField()),
                ('Essn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
                ('Pno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
            ],
        ),
    ]
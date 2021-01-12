# Generated by Django 3.1.5 on 2021-01-11 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_employee', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorksOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hours', models.CharField(max_length=250)),
                ('Essn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('Pno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_employee.projectemployee')),
            ],
            options={
                'verbose_name_plural': 'Works On',
            },
        ),
    ]

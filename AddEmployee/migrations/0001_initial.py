# Generated by Django 3.2.19 on 2023-06-30 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('employeeid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='AddEmployee.identity')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_designation', to='AddEmployee.identity')),
            ],
        ),
    ]
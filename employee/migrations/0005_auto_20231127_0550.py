# Generated by Django 3.2.12 on 2023-11-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employeesalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='EmployeeSalary',
        ),
    ]

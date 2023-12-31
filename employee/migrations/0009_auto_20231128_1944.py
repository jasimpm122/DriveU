# Generated by Django 3.2.12 on 2023-11-28 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_rename_employeleave_employeeleave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='EmployeeSalary',
            new_name='Salary',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.manager'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='EmployeeLeave',
        ),
        migrations.AddField(
            model_name='leave',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]

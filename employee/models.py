from django.db import models
#
#
# class Department(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Manager(models.Model):
#     name = models.CharField(max_length=200)
#     department = models.ForeignKey(Department, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return self.name
#
#
# class Employee(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#
#     name = models.CharField(max_length=200)
#     dob = models.DateField(blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     mobile_number = models.CharField(max_length=10)
#     manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
#     designation = models.CharField(blank=True, null=True, max_length=200)
#     marital_status = models.CharField(blank=True, null=True, max_length=20)
#     age = models.PositiveSmallIntegerField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     address = models.TextField(blank=True, null=True)
#     doj = models.DateField()
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#
# class EmployeeSalary(models.Model):
#     day = models.DateField()
#     salary = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ("employee", "day")
#
#     def __str__(self):
#         return self.employee.name
#
#
# class EmployeeLeave(models.Model):
#     day = models.DateField()
#     time = models.TimeField()
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.employee.name
# from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=200)
    dob = models.SmallIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile_number = models.IntegerField()
    doj = models.DateField()
    address = models.TextField(blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    age = models.PositiveSmallIntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Salary(models.Model):
    day = models.DateField()
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('employee', 'day')

    def __str__(self):
        return self.employee.name


class Leave(models.Model):
    day = models.DateField()
    Time = models.TimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.name





from django.contrib import admin

from employee.models import Department, Manager, Employee, Salary, Leave

admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Leave)




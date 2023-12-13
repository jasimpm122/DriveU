from django.urls import path

from employee.views import listing_employees, add_employee, delete_employee

urlpatterns = [

    # path("employee/managers/", managers_list),
    # path("employee/employees/", employees_list),
    # path("employee/leave/", leave_list),
    # path("employee/managers/v2/", managers_list_v2),
    # path("employee/salary/", salary_list),
    path("employee/list/", listing_employees, name="list_employees"),
    path("employee/add/", add_employee, name="add_employee"),
    path("employee/delete", delete_employee, name="delete_employee")
]

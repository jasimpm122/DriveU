# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
# from employee.models import Manager
# from employee.models import Employee
from django.urls import reverse

# def managers(request):
#     return JsonResponse({
#         "status": "success",
#         "managers": [{
#             "id": i.id,
#             "name": i.name,
#             'department': {
#                 'id': i.department.id,
#                 'name': i.department.name
#             }
#         } for i in Manager.objects.all()]
#     })
#
#
# def employees_list(request):
#     employees = []
#     for x in Employee.objects.all():
#         employees.append({
#             "id": x.id,
#             "name": x.name,
#             'designation': x.designation,
#             'gender': x.gender,
#             'gender_display': x.get_gender_display(),
#             'email': x.email,
#             'manager': {
#                 'name': x.manager.name
#             }
#         })
#     return JsonResponse(employees, safe=False)
#
#
# def bangalore(request):
#     return HttpResponse("Hello bangalore")
# from django.http import JsonResponse
#
# from employee.models import Employee
# from employee.models import Manager


# def managers_list(request):
#     managers = []
#     for x in Manager.objects.all():
#         managers.append({
#             "id": x.id,
#             "name": x.name,
#             "department": {
#                 "name": x.department.name
#             }
#         })
#
#     return JsonResponse(managers, safe=False)


# def employees_list(request):
#     employees = []
#     for i in Employee.objects.all():
#         employees.append({
#             "id": i.id,
#             "name": i.name,
#             "designation": i.designation,
#             "gender": i.gender,
#             "mobile": i.mobile_number,
#             "gender_display": i.get_gender_display(),
#             "manager": {
#                 "name": i.manager.name
#             }
#         })
#     return JsonResponse(employees, safe=False)
#
#
# def managers_list(request):
#     managers = []
#     for x in Manager.object.all():
#         managers.append({
#             "id": x.id,
#             "manager": x.name,
#             "department": {
#                 "name": x.department.name
#             }
#         })
#     return JsonResponse(managers, safe=False)
from employee.models import Employee
from employee.models import Manager
from employee.models import Leave, Salary

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm


# from django.core.serializers import serialize


# def managers_list(request):
#     b = list(Manager.objects.filter(department__name="IT").values())
#     return JsonResponse(b, safe=False)
#
#
# def employees_list(request):
#     x = list(Employee.objects.filter(manager__name="shafi").values())
#     return JsonResponse(x, safe=False)
#
#
# def leave_list(request):
#     a = list(Leave.objects.filter(employee__name="hadik").values())
#     return JsonResponse(a, safe=False)
#
#
# def managers_list_v2(request):
#     i = list(Manager.objects.values())
#     return JsonResponse(i, safe=False)
#
#
# def salary_list(request):
#     c = list(Salary.objects.filter(employee__name="hameez").values())
#     return JsonResponse(c, safe=False)


def listing_employees(request):
    all_employees = Employee.objects.all()
    return render(request, "employee_listing.html", {
        'objects': all_employees
    })


# def listing_employees_v2(request):
#     all_empl  oyees_v2 = Employee.objects.all()
#     return render(request, "employee_detailesv2.html", {
#         'employees_v2': all_employees_v2
#     })


def delete_employee(request, employee_id):
    i = Employee.objects.get(id=employee_id)
    i.delete()
    return redirect(reverse('list_employees'))



def add_employee(request):

    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employees')
    elif request.method == 'GET':
        form = EmployeeForm()

    return render(request, 'employee_detailesv2.html', {'form': form})

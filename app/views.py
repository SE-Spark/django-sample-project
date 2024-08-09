from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee
from .forms import EmployeeForm


def index(request):
    query = request.GET.get('q')
    if query and query.strip():
        employee_list = Employee.objects.filter(name__icontains=query).order_by('id')
        request.session['search_query'] = query
    else:
        query = request.session['search_query'] = ''
        employee_list = Employee.objects.order_by("id")
    return render(request, 'employees/employee_list.html', {'employee_list': employee_list, 'search_query': query})


def employee_detail(request, employee_id):
    # Retrieve the employee object from the database
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


def add_employee(request):
    if request.method == 'POST':
        # If the form has been submitted
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the employee list page or any other page
            return redirect('employee_list')
    else:
        # If the form is not submitted, create a blank form
        form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {'form': form})


def edit_employee(request, employee_id):
    # Retrieve the employee instance from the database
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        # If the form has been submitted with data
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            # Save the updated form data to the database
            form.save()
            # Redirect to the employee detail page or any other page
            return redirect('employee_detail', employee_id=employee_id)
    else:
        # If the form is not submitted, populate the form with existing employee data
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/employee_form.html', {'form': form})


def delete_employee(request, employee_id):
    # Retrieve the employee instance from the database
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        # If the request method is POST, delete the employee instance
        employee.delete()
        # Redirect to the employee list page or any other page
        return redirect('employee_list')

    # Render a confirmation page for deleting the employee
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

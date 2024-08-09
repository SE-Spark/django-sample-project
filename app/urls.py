from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="employee_list"),
    path("<int:employee_id>/view/", views.employee_detail, name="employee_detail"),
    path("<int:employee_id>/delete/", views.delete_employee, name="delete_employee"),
    path("add/", views.add_employee, name="add_employee"),
    path("<int:employee_id>/edit/", views.edit_employee, name="edit_employee")
]

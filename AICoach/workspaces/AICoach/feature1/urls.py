from django.urls import path

from .views import EmployeeCrudView

urlpatterns = [
    path('/', EmployeeCrudView.as_view(), name='employee_crud'),
]


from django import forms

from ..packages.crud.forms import BaseForm, BaseSimpleForm
from ..packages.crud.form_fields import  ModelField

from .models import Employee

class EmployeeForm(BaseForm):
    first_name = ModelField(placeholder="Enter First Name", required=True, required_msg="This field is required.")
    last_name = ModelField(placeholder="Enter Last Name", required=True, required_msg="This field is required.")
    date_of_joining = ModelField(placeholder="Enter Date of Birth", required=True, required_msg="This field is required.")
    gender = ModelField(placeholder="Select Gender", required=True, required_msg="This field is required.")
    address = ModelField(placeholder="Enter Address", required=False)
    phone_number = ModelField(placeholder="Enter Phone Number", required=False)
    email = ModelField(placeholder="Enter Email", required=False)
    years_of_experience = ModelField(placeholder="Enter Years Of Experience", required=False)
    time_off_days  = ModelField(placeholder="Enter Total time offs per year for this employee", required=False)

    class Meta:
        title = "Employee"
        model = Employee


class EmployeeDeactivateForm(BaseSimpleForm):
    reason = forms.CharField(label="Reason", max_length=100, required=False)
    date = forms.DateField(label="Date", required=True)
    file = forms.FileField(label="Resignation Letter", required=False)

    class Meta:
        title = "Terminate Employee"

        order = ["date", "reason", "file"]

    def save(self):
        pass

class EmployeeLeaveForm(BaseSimpleForm):
    reason = forms.CharField(label="Reason", max_length=100, required=False)
    no_of_days = forms.IntegerField(label="No of days required", required=True)

    class Meta:
        title = "Grant Time Off"

        order = ["no_of_days", "reason"]

    def save(self):
        pass
      

import datetime

from ..packages.workflow.base.engine import WorkflowBase

from .forms import EmployeeDeactivateForm, EmployeeLeaveForm
from .models import Employee



class EmployeeWorkflow(WorkflowBase):
    status_transitions = [
        {
            "name": "terminate",
            "display_name": "Terminate",
            "description": "Terminate the employee",
            "from": "active",
            "to": "terminated",
            "form": EmployeeDeactivateForm,
        },
        {
            "name": "activate",
            "from": "terminated",
            "to": "active",
            "display_name": "Activate",
            "description": "Activate the Employee",
            "confirmation_message": "Are you sure you want to activate the employee?",
        },
        {
            "name": "time_off",
            "display_name": "Grant Time Off",
            "description": "Allow the employee some time off",
            "from": "active",
            "to": "on_leave",
            "form": EmployeeLeaveForm,
        },
        {
            "name": "activate",
            "from": "on_leave",
            "to": "active",
            "display_name": "Activate",
            "description": "Activate the Employee",
            "confirmation_message": "Are you sure you want to activate the employee?",
        },
    ]

    def terminate_condition(self, request, object_instance, **kwargs):
        return not object_instance.termination_date
    
    # employee termination date should be the date given in the submitted form or today's date
    def terminate_done(self, request, object_instance, transaction_obj):
        date = request.POST.get("date")
        if date:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            object_instance.termination_date = date_obj
        else:
            object_instance.termination_date = datetime.date.today()
        object_instance.save()
        pass

    def activate_condition(self, request, object_instance, **kwargs):
        return True

    def activate_done(self, request, object_instance, transaction_obj):
        # active employee should not have a termination date.
        if object_instance.termination_date:
            object_instance.termination_date = None
            object_instance.save()
        pass
    
    # employee needs to have time off days left to be given time off.
    def time_off_condition(self, request, object_instance, **kwargs):
        return object_instance.time_off_days > 0  
    
    # when employee takes days off those days need to be subtracted from time off days left.
    def time_off_done(self, request, object_instance, transaction_obj): 
        days = int(request.POST.get("no_of_days"))
        if object_instance.time_off_days >= days:
            object_instance.time_off_days -= days
            object_instance.save()
        pass

    class Meta:
        statuses = {
            "active": {
                "color": "#90ee90",
                "label": "Active",
            },
            "on_leave": {
                "color": "#ffff00",
                "label": "On Leave",
            },
            "terminated": {
                "color": "#FF0000",
                "label": "Terminated",
            },
        }
        model = Employee
        on_create_status = "active"
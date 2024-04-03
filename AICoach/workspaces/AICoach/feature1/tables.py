from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol

from .models import Employee
from .forms import EmployeeForm

class EmployeeTable(ModelTable):
    first_name = ModelCol(display_as='First Name', sortable=True, searchable=True)
    last_name = ModelCol(display_as='Last Name', sortable=True, searchable=True)
    date_of_joining = ModelCol(display_as='Date of Joining', sortable=True, searchable=True)
    gender = ModelCol(display_as='Gender', sortable=True, searchable=True)
    address = ModelCol(display_as='Address', sortable=False, searchable=True)
    phone_number = ModelCol(display_as='Phone Number', sortable=False, searchable=True)
    email = ModelCol(display_as='Email', sortable=False, searchable=True)
    years_of_experience = ModelCol(display_as='Experience (Years)', sortable=False, searchable=True)
    time_off_days = ModelCol(display_as='Time off Days left', sortable=False, searchable=True)

    table_actions = []
    row_actions = [
            {
                "name": "Edit",
                "key": "edit",
                "description": "Edit Employee",
                "type": "form",
                "form": EmployeeForm,
                "roles": ["Manager"]  # Manager can edit employee
            },
            {
                "name": "Delete",
                "key": "delete_employee",
                "description": "Delete Employee",
                "type": "simple",
                "confirmation_message": "Are you sure you want to delete this employee?",
                "roles": ["Manager"] # Manager can delete employee
            }
        ]
    
    def process_row_action_delete_employee(self, request, obj):
        success = False
        
        if obj.years_of_experience > 5:
            response = {
                "Permission Denied": "You can't delete employees with more than 5 years of experience"
            }
        else:
            obj.delete()
            response = {
                "Operation Completed": "Employee has been deleted" 
            }
            success = True

    
        return success, response

    class Meta:
        model = Employee
        fields = [
                'first_name', 'last_name', 'date_of_joining', 'gender', 
                'address', 'phone_number', 'email', 'years_of_experience',
                'time_off_days'
            ]
        row_selector = {'enabled': False, 'multi': False}
        

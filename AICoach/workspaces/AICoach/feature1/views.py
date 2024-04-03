from .forms import EmployeeForm
from .tables import EmployeeTable
from .workflow import EmployeeWorkflow

from ..packages.crud.base import BaseCrudView

    
class EmployeeCrudView(BaseCrudView):
    page_title = "Employees"
    add_btn_title = "Add New Employee"
    table = EmployeeTable
    form = EmployeeForm
    workflow = EmployeeWorkflow
    

    #only manager can add new employees
    def display_add_button_check(self, request):   
    
        from zelthy.core.utils import get_current_role     
        
        role = get_current_role()
        
        if role:
            return role.name in ["Manager"]
        
        return False


    
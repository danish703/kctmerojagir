from employee.models import Employee
from company.models import Company
def isemployee(user_id):
    try:
        Employee.objects.get(user_id=user_id)
        return True
    except:
        return False


def isCompany(user_id):
    try:
        Company.objects.get(user=user_id)
        return True
    except:
        return False

from employee.models import Employee
def isemployee(user_id):
    try:
        Employee.objects.get(user_id=user_id)
        return True
    except:
        return False

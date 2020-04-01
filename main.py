from employee import Employee

employee = Employee()
employee.hasAchievedTarget();
print("name: ",employee.name)


employeeOne = Employee()
employeeTwo = Employee()
print("Assign value to all object")

Employee.job = "Security"
print("Object 1: ", employeeOne.job)
print("Object 2: ", employeeTwo.job)


print("Assign value to one object")

employeeOne.job = "Programmer"
print("Object 1: ", employeeOne.job)
print("Object 2: ", employeeTwo.job)


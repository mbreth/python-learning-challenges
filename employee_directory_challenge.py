employees = [
  {
    'employee_id': 101,
    'employee_name': 'John Smith',
    'department': 'Engineering',
    'salary': 85000
  },
  {
    'employee_id': 102,
    'employee_name': 'Sarah Johnson',
    'department': 'Quality',
    'salary': 72000
  },
  {
    'employee_id': 103,
    'employee_name': 'Mike Davis',
    'department': 'Production',
    'salary': 65000
  } 
]

menu = ["1. View all employees", "2. Search employee by ID", "3. Add new employee", "4. Search by Department", "5. Exit"]

for i in menu:
    print(i)

user_input = 0

def view_employees():
  for employee in employees:
    print(f"{employee['employee_id']} - {employee['employee_name']} - {employee['department']} - ${employee['salary']:,.2f}")

def search_employee_id():
  id_num = int(input("Enter employee id: "))
  found_id = 0
  for employee in employees:
    if employee['employee_id'] == id_num:
      found_id += 1
      print("Employee found!")
      print(f"Name: {employee['employee_name']}")
      print(f"Department: {employee['department']}")
      print(f"Salary: ${employee['salary']:,.2f}")
  if found_id == 0:
    print("Employee not found!")

def add_new_employee():
  new_id = 0000
  while new_id == 0000:
    new_id = int(input("Please enter the employee id: "))
    for id in employees:
      if id['employee_id'] == new_id:
        print("That employee ID is already taken!")
        new_id = 0000
  new_name = input("Please enter the employee name: ")
  new_dpt = input("Please enter department: ")
  new_salary = int(input("Please enter the salary: "))
  employees.append({'employee_id': new_id, 'employee_name': new_name, 'department': new_dpt, 'salary': new_salary})
  print("Employee added successfully!")

def find_by_dept():
  dpt_srch = "null"
  found_dpt = 0
  while dpt_srch == "null":
    dpt_srch = input("Please enter a department: ")
    for dpts in employees:
      if dpts['department'] == dpt_srch.capitalize():
        found_dpt += 1
        print(f"Employees in {dpt_srch.capitalize()} department: {dpts['employee_name']}")
    if found_dpt == 0:
      print(f"Department {dpt_srch.capitalize()} was not found!")
        
    
while user_input != 5:
  user_input = int(input("Please select an option: "))
  if user_input == 1:
    view_employees()
  elif user_input == 2:
    search_employee_id()
  elif user_input == 3:
    add_new_employee()
  elif user_input == 4:
    find_by_dept()
  elif user_input <= 0 or user_input > 5:
    print("Not a valid input!")

print("Goodbye!")

    
      

















      

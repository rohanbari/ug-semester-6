employees = {
    "Aarav": 7200,
    "Ananya": 4800,
    "Aditya": 5100,
    "Bhavna": 4500,
    "Charan": 6200,
    "Divya": 3900,
    "Eshan": 5300,
    "Farah": 4700,
    "Gopal": 8000,
    "Harini": 4950,
}

# a. Print the names of employees starting with A.
names_starting_with_a = [name for name in employees if name.startswith("A")]
print("Employees starting with A:", names_starting_with_a)

# b. Display the highest salary.
highest_salary = max(employees.values())
print("Highest salary:", highest_salary)

# c. Display names of employees with salary below Rs. 5000.
below_5000 = [name for name, salary in employees.items() if salary < 5000]
print("Employees with salary below Rs. 5000:", below_5000)

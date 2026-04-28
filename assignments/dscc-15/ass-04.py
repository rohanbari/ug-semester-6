class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = years_of_service

    def salary(self):
        return 1500 + 100 * self.years_of_service


class Manager(Employee):
    def salary(self):
        return 2500 + 120 * self.years_of_service


def main():
    # Creating dictionary database
    db = {
        "Rahul": Employee("Rahul", 3),
        "Bikash": Employee("Bikash", 1),
        "Rajan": Manager("Rajan", 10),
        "Priya": Manager("Priya", 3)
    }

    # Creating table [name, salary]
    table = []
    total_salary = 0

    for name, obj in db.items():
        sal = obj.salary()
        table.append([name, sal])
        total_salary += sal

    # Average salary
    avg_salary = total_salary / len(db)

    # Output
    print("Employee Salary Table:")
    for row in table:
        print(row)

    print("Average Salary:", avg_salary)


if __name__ == "__main__":
    main()

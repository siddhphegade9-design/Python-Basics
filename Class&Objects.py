class Employee:

    Company = "Seagate"

    def __init__(self, name, salary, contract):
        self.name = name
        self.salary = salary
        self.contract = contract

    def show_employee(self):
        print("Name:", self.name, "Salary:", self.salary, "Contract:", self.contract)

    def get_salary(self):
        return self.salary

    # Instance Method
    def print_info(self):
        info = f"Name: {self.name}, Salary: {self.salary}, Contract: {self.contract}"
        print(info)

    # Static Method
    @staticmethod
    def summ(a, b):
        return a + b

    # Class Method
    @classmethod
    def get_company(cls):
        print("Company:", cls.Company)

    @classmethod
    def set_company(cls, new_company):
        cls.Company = new_company


First = Employee("Nikhil", 100000, "Permanent")
First.show_employee()

print(First.get_salary())

print(First.Company)
print(First.name)

First.print_info()
print(Employee.summ(5, 3))

First.get_company()
First.set_company("TCS")  # Changes the value for the whole class
First.get_company()
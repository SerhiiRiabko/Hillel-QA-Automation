class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.addresses = []
        self.company = 'BMW'

    def update_empl_company(self, new_company):
        self.company = new_company

    @staticmethod
    def show_holidays():
        print('10.01, 08.05, 28.06')

    @classmethod
    def create_employee_with_bonus(cls, name, age, salary, bonus):
        salary_with_bonus = salary + bonus
        return cls(name, age, salary_with_bonus)


if __name__ == '__main__':
    john = Employee('John', 24, 5000)
    marta = Employee('Marta', 23, 7000)

    print(john.addresses.append('Scriabin 25'))
    print(john.addresses)
    print(marta.addresses)

print(Employee.show_holidays())

john_with_bonus = Employee.create_employee_with_bonus('JonhB', 34, 1400, 700)

print(john_with_bonus.salary)



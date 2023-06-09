class Worker:
    def __init__(self, name: str, position: str, salary: float):
        self._name = name
        self._position = position
        self._salary = salary

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if self._name is True and len(self._name) > 0:
            self._name = value
        else:
            print('Please the name. It can\'t be empty')

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str):
        if len(self._position) > 0:
            self._position = value
        else:
            print('Position can\'t be empty')

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if self._salary > 0 and type(self.salary) is float:
            self._salary = value
        else:
            print('Salary should be float and more than 0!!!')

    @classmethod
    def from_dict(cls, worker_dict):
        return cls(
            name=worker_dict.get('name'),
            position=worker_dict.get('position'),
            salary=worker_dict.get('salary')
        )

    @staticmethod
    def is_high_salary(salary):
        return salary > 10000

    def get_worker_info(self) -> str:
        return f"Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary:.2f}"


worker = Worker("John Doe", "Engineer", 5000.0)
print(worker.get_worker_info())

worker_dict = {
    'name': 'John Veek',
    'position': 'Manager',
    'salary': 12000.0
}
worker_from_dict = Worker.from_dict(worker_dict)
print(worker_from_dict.get_worker_info())

print(Worker.is_high_salary(15000.0))

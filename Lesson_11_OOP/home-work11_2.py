class Worker:


    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary


def get_worker_info(self) -> str:
    return f"Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary:.2f}"


worker = Worker("John Doe", "Engineer", 5000.0)

print(worker.get_worker_info())

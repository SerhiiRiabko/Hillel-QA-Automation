name = 'Garry'
age = 18
salary = 3200


# Class

class Employees:
    pass
    # якщо пропишемо змінні всередині будуть статичні атрибути


john = Employees()
marta = Employees()


class Employees2:
    COMPANY = 'BMW'


john = Employees2()
john.COMPANY
marta = Employees2()
marta.COMPANY
# Add too class only for marta
marta.status = 'Married'
print(marta.status)




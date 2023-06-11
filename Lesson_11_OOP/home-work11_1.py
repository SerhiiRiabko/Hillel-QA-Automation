class Company:
    def __init__(self, name, industry, location):
        self._name = name
        self._industry = industry
        self._location = location

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def get_company_info(self):
        return f"Company: {self.name}, Industry: {self.industry}, Location: {self.location}"

    @classmethod
    def create_company(cls, name, industry, location):
        return cls(name, industry, location)

    @staticmethod
    def print_static_info():
        print("This is a static method in the Company class")

    @staticmethod
    def is_valid_company_name(name):
        return len(name) > 0


company = Company("Apple", "Technology", "California")
print(company.get_company_info())


company2 = Company.create_company("Toshiba", "Technology", "Osaka")
print(company2.get_company_info())

Company.print_static_info()


print(Company.is_valid_company_name("Apple"))

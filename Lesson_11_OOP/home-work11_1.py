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
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Length can't be empty or not String")

    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._industry = value
        else:
            raise ValueError("Length can't be empty or not String")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._location = value
        else:
            raise ValueError("Length can't be empty or not String")

    def get_company_info(self):
        return f"Company: {self._name}, Industry: {self._industry}, Location: {self._location}"

    @classmethod
    def create_company(cls, name, industry, location):
        if name or industry or location is str:
            return cls(name, industry, location)
        else:
            print('You have some mistakes')

    @staticmethod
    def print_static_info():
        company_some = Company()
        if company_some.create_company() is True:
            print('You may add employees')
        else:
            print('Company is not created')

    @staticmethod
    def is_valid_company_name(name):
        return len(name) > 0


if __name__ == '__main__':
    company = Company("Apple", "Technology", "California")
    print(company.get_company_info())
    company2 = Company.create_company("Toshiba", "Technology", "Osaka")
    print(company2.get_company_info())
    print(Company.is_valid_company_name("Apple"))

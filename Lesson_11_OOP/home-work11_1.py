class Company:
    def __init__(self, name, industry, location):
        self.name = name
        self.industry = industry
        self.location = location

    def get_company_info(self):
        return f'Company: {self.name}, Industry: {self.industry}, Location: {self.location}'


company = Company("Apple", "Technology", "California")
company2 = Company("AToshiba", "Technology", "Osaka")

data = company.get_company_info()
print(data)


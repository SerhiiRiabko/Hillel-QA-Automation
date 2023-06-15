from abc import abstractmethod

from autoclass import Auto


class Gm(Auto):
    def __init__(self):
        super().__init__(wheels=4, body='Metal', engine='Power Engines', engine_type='muscle-engine')
        self._main_office_city = 'Detroit'
        self._name = 'GM'
        self._country = 'USA'

    @abstractmethod
    def electricity_problem(self):
        pass

    @abstractmethod
    def simple_repair(self):
        pass

from abc import abstractmethod

from autoclass import Auto


class Vag(Auto):
    def __init__(self):
        super().__init__(wheels=4, body='Metal', engine= 'High Quality', engine_type='Turbo-Compressors')
        self._main_office_city = 'Wolfsburg'
        self._name = 'VAG'
        self._country = 'Germany'

    @abstractmethod
    def work_long_without_crash(self):
        pass

    @abstractmethod
    def hard_repair(self):
        pass

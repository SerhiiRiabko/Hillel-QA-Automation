from abc import abstractmethod

from autoclass import Auto


class ToyotaCo(Auto):
    def __init__(self):
        super().__init__(wheels=4, body='Metal', engine='reliable', engine_type='fuel')
        self._main_office_city = 'Toyota(IT)'
        self._name = 'Toyota'
        self._country = 'Japan'

    @abstractmethod
    def latest_developments(self):
        pass

    @abstractmethod
    def reliable(self):
        pass

# Singleton
from singleton_decorator import singleton
from singleton_meta import SingleTonMeta


@singleton
class DbConnector:

    # _instance{}

    def __init__(self, db_pass, db_name):
        self.db_pass = db_pass
        self.db_name = db_name


if __name__ == '__main__':
    db_connector = DbConnector('123', 'toys')
    db_connector2 = DbConnector('123', 'toys')

    print(db_connector is db_connector2)


# meta


class DbConnector(metaclass=SingleTonMeta):

    def __init__(self, db_pass, db_name):
        self.db_pass = db_pass
        self.db_name = db_name


if __name__ == '__main__':
    db_connector = DbConnector('123', 'toys')
    db_connector2 = DbConnector('123', 'toys')

    print(db_connector is db_connector2)

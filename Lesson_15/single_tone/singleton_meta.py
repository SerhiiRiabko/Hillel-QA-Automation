class SingleTonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instace:
            instance = super().__call__(*args, **kwargs)
            cls._instace[cls] = instance
        return cls._instances[cls]

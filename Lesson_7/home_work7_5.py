from typing import Iterable


def custom_all(iterable: Iterable) -> bool:
    for element in iterable:
        if not element:
            return False
    return True

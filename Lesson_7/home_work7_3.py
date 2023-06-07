from typing import Callable, Sequence, Any, List


def custom_map(callback: Callable[[Any], Any], sequence: Sequence) -> List:
    new_list = []
    for element in sequence:
        result = callback(element)
        new_list.append(result)
    return new_list

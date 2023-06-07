from typing import Callable, Sequence, Union


def filter_custom(callback: Callable[[Union[int, float, str]], bool], sequence: Sequence[Union[int, float, str]]) -> \
        Sequence[Union[int, float, str]]:
    result = []
    for item in sequence:
        if callback(item):
            result.append(item)
    return result

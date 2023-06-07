from typing import Any, List, Optional


def custom_max(sequence: List[Any], amount: Optional[int] = 1) -> List[Any]:
    sorted_sequence = sorted(sequence, reverse=True)
    return sorted_sequence[:amount]


def custom_min(sequence: List[Any], amount: Optional[int] = 1) -> List[Any]:
    sorted_sequence = sorted(sequence)
    return sorted_sequence[:amount]

def min_arrow_rotations(S: str) -> int:
    arrow_counts = {'^': 0, 'v': 0, '<': 0, '>': 0}

    for arrow in S:
        arrow_counts[arrow] += 1

    max_count = max(arrow_counts.values())
    return len(S) - max_count

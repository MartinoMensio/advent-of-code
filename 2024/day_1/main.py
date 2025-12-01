import re
from collections import defaultdict
from typing import List, Tuple

from advent_of_code_2024.utils.advent_helper import get_input_for_day


def parse_input(input_text: str) -> Tuple[List, List]:
    a = []
    b = []
    for line in input_text.splitlines():
        match = re.match(r"(\d+) +(\d+)", line)
        if not match:
            raise ValueError(f"Could not parse line: {line}")
        val_a, val_b = match.groups()
        a.append(int(val_a))
        b.append(int(val_b))
    return a, b


def distance_sorted_lists(a: List, b: List) -> int:
    return sum(abs(x - y) for x, y in zip(a, b))


def part_1(a: List, b: List) -> int:
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    result = distance_sorted_lists(sorted_a, sorted_b)
    return result


def part_2(a: List[int], b: List[int]) -> int:
    b_count_by_value = defaultdict(int)
    for value in b:
        b_count_by_value[value] += 1
    distance = 0
    for value in a:
        distance += value * b_count_by_value[value]
    return distance


def main():
    input_text = get_input_for_day(1)
    a, b = parse_input(input_text)
    result_part_1 = part_1(a, b)
    print("Result part 1:", result_part_1)
    result_part_2 = part_2(a, b)
    print("Result part 2:", result_part_2)


if __name__ == "__main__":
    main()

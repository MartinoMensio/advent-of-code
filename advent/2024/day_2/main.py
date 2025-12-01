from typing import List, Tuple

from advent_of_code_2024.utils.advent_helper import get_input_for_day


def parse_input(input_text: str) -> List[List[int]]:
    result = []
    for line in input_text.splitlines():
        values = [int(value) for value in line.split()]
        result.append(values)
    return result


def part_1(values: List[List[int]]) -> int:
    safe_count = 0
    for row in values:
        internal_diff = [row[i] - row[i - 1] for i in range(1, len(row))]
        are_diffs_positive = [val > 0 for val in internal_diff]
        are_diffs_negative = [val < 0 for val in internal_diff]
        if any(are_diffs_positive) and any(are_diffs_negative):
            # increasing and decreasing at the same time
            # print("Row:", row, "increasing and decreasing", internal_diff)
            continue
        if any([val == 0 or val > 3 or val < -3 for val in internal_diff]):
            # difference too big or zero
            # print("Row:", row, "difference too big or zero", internal_diff)
            continue
        # print("Row:", row, "safe", internal_diff)
        safe_count += 1
    return safe_count


def part_2(values: List[List[int]]) -> int:
    # TODO: Problem Dampener
    safe_count = 0
    for row in values:
        internal_diff = [row[i] - row[i - 1] for i in range(1, len(row))]
        are_diffs_positive = [val > 0 for val in internal_diff]
        are_diffs_negative = [val < 0 for val in internal_diff]
        if len(are_diffs_positive) and any(are_diffs_negative):
            # increasing and decreasing at the same time
            print("Row:", row, "increasing and decreasing", internal_diff)
            continue
        if any([val == 0 or val > 3 or val < -3 for val in internal_diff]):
            # difference too big or zero
            print("Row:", row, "difference too big or zero", internal_diff)
            continue
        print("Row:", row, "safe", internal_diff)
        safe_count += 1
    return safe_count


def main():
    input_text = get_input_for_day(2)
    #     input_text = """
    # 7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9
    # """.strip()
    values = parse_input(input_text)
    result_part_1 = part_1(values)
    print("Result part 1:", result_part_1)
    result_part_2 = part_2(values)
    print("Result part 2:", result_part_2)


if __name__ == "__main__":
    main()

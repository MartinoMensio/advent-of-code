from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Tuple

import typer
from tqdm import tqdm

current_path = Path(__file__).parent

def read_rows(input_path: Path) -> Iterator[List[int]]:
    with open(input_path) as f:
        for line in f:
            yield parse_row(line.strip())

def parse_row(line: str) -> List[int]:
    batteries = [int(el) for el in line]
    return batteries

def select_best_batteries(row: List[int], amount: int=2, debug: bool = False) -> int:
    # best = sorted(row, reverse=True)[:amount]
    best = 0
    for i, v_i in enumerate(row):
        for j, v_j in enumerate(row[i+1:]):
            val = v_i*10 + v_j
            if val > best:
                best = val
                # print(v_i, v_j)
    if debug:
        print(f"row best {best}")
    return best

def select_best_recursive(row: List[int], amount: int, max_index_allowed: Optional[int] = None, debug: bool = False) -> Optional[int]:
    if max_index_allowed is None:
        max_index_allowed = len(row)
    prefix = "".join([" "] * (12 - amount))
    if debug:
        print(prefix, f"row: {row}, amount: {amount}")
    if len(row) < amount:
        # not valid
        return None
    best = -1
    if amount == 1:
        return max(row)
    for i, v_i in enumerate(row):
        if i > max_index_allowed:
            # pruning
            break
        new_amount = amount -1
        start = i+1
        end = len(row) - new_amount + 1
        sublist = row[start:]
        if debug:
            print(prefix, f"sublist for recursion {i}={v_i} [{start}:]", sublist, f"max_index_allowed: {end}")
        sub_best = select_best_recursive(sublist, amount=new_amount, max_index_allowed=end, debug=debug)
        if sub_best:
            val = int(str(v_i) + str(sub_best))
            if debug:
                print(prefix, "sub_best", val, sub_best)
            if val > best:
                best = val
                if debug:
                    print(prefix, "new best", row, best, sub_best, amount)
    if debug:
        print(prefix, row, "best", best)
    return best

def max_subsequence_value(row: List[int], k: int) -> int:
    # this time with stack, recursive is too slow
    stack: List[int] = []
    n = len(row)
    # how many digits we are allowed to drop
    to_drop = n - k
    for d in row:
        while stack and to_drop > 0 and stack[-1] < d:
            stack.pop()
            to_drop -= 1
        if len(stack) < k:
            stack.append(d)
        else:
            # if stack already full, skip this digit and (conceptually) one less drop available
            # but we must not let to_drop become negative
            to_drop = max(to_drop - 1, 0)
    # ensure length is exactly k (slice if needed)
    stack = stack[:k]
    # convert digits to integer quickly
    val = 0
    for digit in stack:
        val = val * 10 + digit
    return val



def main(
        input_path: Path = current_path / "mock_data.txt",
        debug: bool = False,
        amount: int = 2,
):
    rows = read_rows(input_path)
    rows = list(rows)
    total = 0
    for row in tqdm(rows):
        # best_batteries = select_best_batteries(row, debug=debug)
        # best_batteries = select_best_recursive(row, amount=amount, debug=debug)
        best_batteries = max_subsequence_value(row, k=amount)
        total += best_batteries

    print("total", total)

if __name__ == "__main__":
    typer.run(main)
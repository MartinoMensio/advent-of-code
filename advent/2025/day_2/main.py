from pathlib import Path
from typing import Iterable, Iterator, List, Tuple

import typer

current_path = Path(__file__).parent

def read_ranges(input_path: Path) -> Iterator[Tuple[int,int]]:
    with open(input_path) as f:
        for line in f:
            chunks = line.split(",")
            for chunk in chunks:
                start, end = chunk.split("-")
                yield int(start), int(end)

def find_invalids(ranges: Iterator[Tuple[int,int]], debug: bool = False, part_2: bool = False) -> Iterator[int]:
    for range_val in ranges:
        if debug:
            print(f"range {range_val}")
        for value in range(range_val[0], range_val[1] + 1):
            if check_invalid_value(value, debug=debug, part_2=part_2):
                if debug:
                    print(f"invalid {value}")
                yield value

def check_invalid_value(value, debug: bool = False, part_2: bool = False) -> bool:
    # if debug:
    #     print(f"checking {value}")
    digits = str(value)
    length = len(digits)
    if not part_2:
        if not length % 2 == 0:
            if debug:
                print(f"{value} number with odd #digits ({length}) cannot be invalid")
            return False
        half = length // 2
        return digits[:half] == digits[half:]
    else:
        for sublength in range(length // 2, 0, -1):
            pieces = list(chunks(digits, sublength))
            if debug:
                print(f"  {digits} in sublength {sublength}: {pieces}")
            if len(set(pieces)) == 1:
                return True
        return False

def chunks(L: list | str, n: int):
    """ Yield successive n-sized chunks from L.
    """
    for i in range(0, len(L), n):
        yield L[i:i+n]



def main(
        input_path: Path = current_path / "mock_data.txt",
        debug: bool = False,
        part_2: bool =False,
):
    rows = read_ranges(input_path)
    invalids = find_invalids(rows, debug=debug, part_2=part_2)
    sum_invalids = sum(invalids)
    print("sum_invalids", sum_invalids)

if __name__ == "__main__":
    typer.run(main)
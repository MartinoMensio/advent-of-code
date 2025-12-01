from pathlib import Path
from typing import Iterator, List

import typer

current_path = Path(__file__).parent

class Dial:
    position: int
    times_at_0: int
    size: int
    count_inner_ticks: bool
    debug: bool

    def __init__(self, position: int = 50, size: int = 100, count_inner_ticks: bool = True, debug: bool = False):
        self.position = position
        self.times_at_0 = 0
        self.size = size
        self.count_inner_ticks = count_inner_ticks
        self.debug = debug
        self.check_position_at_0()

    def _rotate(self, amount: int):
        self.position = (self.position + amount) % self.size
        self.check_position_at_0()

    def check_position_at_0(self):
        if self.position == 0:
            self.times_at_0 += 1
        if self.debug:
            print(f"position: {self.position} times_at_0: {self.times_at_0}")


    def rotate_left(self, amount: int):
        if self.count_inner_ticks and amount > 1:
            [self._rotate(-1) for _ in range(amount)]
        else:
            self._rotate(amount=-amount)
    
    def rotate_right(self, amount: int):
        if self.count_inner_ticks and amount > 1:
            [self._rotate(1) for _ in range(amount)]
        else:
            self._rotate(amount=amount)


def read_rows(input_path: Path) -> Iterator[dict]:
    with open(input_path) as f:
        for line in f:
            yield parse_row(line)

def parse_row(line: str) -> dict:
    direction = line[0]
    amount = line[1:].strip()
    amount = int(amount)
    # assert amount <=99
    return {
        "direction": direction,
        "amount": amount
    } 

def process_rows(rows: Iterator[dict], count_inner_ticks: bool = True):
    dial = Dial(count_inner_ticks=count_inner_ticks)
    print(dial.count_inner_ticks)
    for row in rows:
        print(f"row: {row}")
        if row["direction"] == "L":
            dial.rotate_left(row["amount"])
        elif row["direction"] == "R":
            dial.rotate_right(row["amount"])
        else:
            raise ValueError(row)
        
    print(dial.times_at_0)


def main(
        input_path: Path = current_path / "mock_data.txt",
        count_inner_ticks: bool = False,
):
    rows = read_rows(input_path)
    process_rows(rows, count_inner_ticks=count_inner_ticks)

if __name__ == "__main__":
    typer.run(main)
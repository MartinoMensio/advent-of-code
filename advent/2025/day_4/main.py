from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Tuple

from typer import Typer

current_path = Path(__file__).parent

app = Typer(pretty_exceptions_enable=False)

def read_matrix(input_path: Path) -> Iterator[List[bool]]:
    with open(input_path) as f:
        for line in f:
            yield parse_row(line.strip())

def parse_row(line: str) -> List[bool]:
    rolls = [el == "@" for el in line]
    return rolls

@app.command()
def main(
        input_path: Path = current_path / "mock_data.txt",
        debug: bool = False,
        keep_doing: bool = False,
):
    matrix = read_matrix(input_path)
    matrix = list(matrix)
    if keep_doing:
        initial_count = sum([el for row in matrix for el in row])
        print(initial_count)
        while True:
            old_count = sum([el for row in matrix for el in row])
            new_matrix = remove_one_step(matrix=matrix, debug=debug)
            new_count = sum([el for row in new_matrix for el in row])
            print(f"old_count:{old_count}, new_count: {new_count}")
            if new_count == old_count:
                break
            matrix = new_matrix
        total_removed = initial_count - new_count
        print("total_removed", total_removed)
    else:
        remove_one_step(matrix=matrix, debug=debug)

def remove_one_step(matrix: List[List[bool]], debug: bool = False) -> List[List[bool]]:
    x_max = len(matrix)
    y_max = len(matrix[0])
    sourrounding_m = [[0 for el in row] for row in matrix]
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if not val:
                # not counting, not a roll
                continue
            if i > 0:
                # row above
                if j > 0:
                    sourrounding_m[i-1][j-1] += 1
                sourrounding_m[i-1][j] += 1
                if j + 1 < y_max:
                    sourrounding_m[i-1][j+1] +=1
            # this row
            if j > 0:
                sourrounding_m[i][j-1] += 1
            # sourrounding_m[i][j] += 1
            if j + 1 < y_max:
                sourrounding_m[i][j+1] +=1
            # next row
            if i + 1 < x_max:
                if j > 0:
                    sourrounding_m[i+1][j-1] += 1
                sourrounding_m[i+1][j] += 1
                if j + 1 < y_max:
                    sourrounding_m[i+1][j+1] +=1
    # now check
    valid = 0
    output_matrix = [[el for el in row] for row in matrix]
    for i, row in enumerate(sourrounding_m):
        for j, val in enumerate(row):
            if matrix[i][j] and val < 4:
                if debug:
                    print(f"remove {i} {j} = {val}")
                valid += 1
                output_matrix[i][j] = False
    print("valid", valid)
    return output_matrix


if __name__ == "__main__":
    app()
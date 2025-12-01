import requests

from advent_of_code_2024.utils.storage import DATA_PATH


def get_input_for_day(day: int) -> str:
    """Get the input for a given day, either from cache or by fetching it."""
    input_path = DATA_PATH / f"day_{day}.txt"
    if not input_path.exists():
        input_text = _fetch_inputs_for_day(day)
        input_path.write_text(input_text)
    return input_path.read_text()


def _fetch_inputs_for_day(day: int) -> str:
    """Fetch the input for a given day."""
    url = f"https://adventofcode.com/2024/day/{day}/input"
    raise ValueError("TODO: implement login!")
    response = requests.get(url)
    print(response.text)
    response.raise_for_status()
    return response.text

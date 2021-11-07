from typing import List, Dict, Tuple

coordinateType = List[Dict[str, Tuple[float, float]]]


def get_coordinates():
    coordinates: coordinateType = [
        {
            'coordinate1': (34.9, 23.23),
        },
        {
            'coordinate2': (87.9, 12.23),
        },
        {
            'coordinate3': (102.9, 9.23),
        }
    ]
    return coordinates


def sum_(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(get_coordinates())
    # print(sum_('3', '5')) this would not be allowed when is run with mypy, because the expected values are integers

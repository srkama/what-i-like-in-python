from typing import Union


def add(a: int, b: int) -> Union[int, None]:
    return None


def add_anothter(a: int, b: int) -> int:
    return None


def find(x, arr: Union[list, tuple, set]) -> bool:
    return True


find(5, (4, 5, 6))
find(5, [1, 2, 3, 4, 5, 6])
find(5, 3)
find(5, {4, 5, 6, 7, 8, 99})

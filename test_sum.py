# test_sum.py
def sum(x: int, y: int) -> int:
    return x + y
...
def test_sum():
    assert sum(3, 4) == 7
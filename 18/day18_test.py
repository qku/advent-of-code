from day18 import *


def test_magnitude_simple():
    assert magnitude([1, 9]) == 21


def test_magnitude_medium():
    assert magnitude([[1,2],[[3,4],5]]) == 143


def test_magnitude_hard():
    assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],
                      [[[0,7],[6,6]],[8,7]]]) == 3488


def test_split():
    number = [[[[0,7],4],[15,[0,13]]],[1,1]]
    p, number = snail_split(number)
    assert number == [[[[0,7],4],[[7,8],[0,13]]],[1,1]]


def test_split_performed():
    number = [[[[0,7],4],[15,[0,13]]],[1,1]]
    p, number = snail_split(number)
    assert p


def test_sum_no_reducing():
    numbers = [[1,1], [2,2], [3,3], [4,4]]
    assert add_numbers(numbers) == [[[[1,1],[2,2]],[3,3]],[4,4]]


def test_reduce():
    number = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    assert reduce(number) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]


def test_sum():
    numbers = read_input('test_input.txt')
    _sum = add_numbers(numbers)
    assert _sum == [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]


def test_sum_magnitude():
    numbers = read_input('test_input.txt')
    _sum = add_numbers(numbers)
    assert magnitude(_sum) == 4140

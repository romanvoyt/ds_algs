import random


def max_num(array):
    if len(array) < 2:
        return array[0]

    max = array[0]
    num = max_num(array[1:])
    if max < num:
        max = num

    return max


def count(array):
    if len(array) < 2:
        return 1
    total = 1 + count(array[1:])
    return total


def arr_sum(array) -> int:
    if len(array) < 2:
        return array[0]

    total = array[0] + arr_sum(array[1:])

    return total


def test_sum():
    l = [random.randint(1, 10) for _ in range(10)]
    print(f'array of numbers : {l}')
    result = arr_sum(l)

    print(f'result : {result}')


def test_count():
    l = [random.randint(1, 10) for _ in range(random.randint(1, 100))]
    print(f'array of numbers : {l}')
    result = count(l)

    print(f'result : {result}')


def test_max_num():
    l = [random.randint(1, 1000
                        ) for _ in range(random.randint(1, 100))]
    print(f'array of numbers : {l}')
    result = max_num(l)

    print(f'max_num result : {result}')
    print(f'built in max func result : {max(l)}')


if __name__ == '__main__':
    test_max_num()


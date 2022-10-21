import random

def count(array) -> int:
    pass


def sum(array) -> int:
    if len(array) < 2:
        return array[len(array)-1]

    total = array[0] + sum(array[1:])

    return total


if __name__ == '__main__':
    l = [random.randint(1,10) for _ in range(10)]
    print(f'array of numbers : {l}')
    result = sum(l)

    print(f'result : {result}')

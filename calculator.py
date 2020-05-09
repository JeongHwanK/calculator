def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def print_result(result):
    print(f'결과: {result}')


if __name__ == "__main__":
    print('원하는 연산을 입력하세요. +, -')
    op = input()
    print('숫자 2개를 입력해주세요')
    a, b = map(int, input().split())

    if op == '+':
        print_result(add(a, b))
    elif op == '-':
        print_result(substract(a, b))

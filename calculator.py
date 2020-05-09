if __name__ == "__main__":
    print('원하는 연산을 입력하세요. +, -, *, %')
    op = input()
    if op == '+':
        print('숫자 2개를 입력해주세요')
        a, b = input().split()
        print(f'결과: {int(a) + int(b)}')
    if op == '-':
        print('숫자 2개를 입력해주세요')
        a, b = input().split()
        print(f'결과: {int(a) - int(b)}')

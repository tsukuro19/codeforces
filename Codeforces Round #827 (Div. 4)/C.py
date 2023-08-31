for _ in range(int(input())):
    abc = input()
    x = [input() for n in range(8)]
    print('R' if 8*'R' in x else 'B')
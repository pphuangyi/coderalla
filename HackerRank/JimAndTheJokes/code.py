def get_digits(number, base):
    digits = []
    while number > 0:
        digit = number % 10
        if digit >= base:
            return None
        digits.append(digit)
        number //= 10
    return digits[::-1]


def get_number(digits, base):
    number = 0
    for digit in digits:
        number *= base
        number += digit
    return number


def solve(dates):
    my_dict = {}
    for base, number in dates:
        if base == 1:
            continue
        digits = get_digits(number, base)
        if digits is not None:
            number_new = get_number(digits, base)
            if number_new in my_dict:
                my_dict[number_new] += 1
            else:
                my_dict[number_new] = 1

    for key, val in my_dict.items():
        print(key, val)
    return sum([val * (val - 1) // 2 for _, val in my_dict.items()])


if __name__ == '__main__':
    input_fname = 'data/input07.txt'
    with open(input_fname, 'r') as handle:
        N = int(handle.readline().strip())
        dates = [list(map(int, handle.readline().strip().split())) for _ in range(N)]
    
    result = solve(dates)
    print(result)
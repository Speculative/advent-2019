lower_bound = 235741
upper_bound = 706948


def digits_increasing(password):
    return int("".join(sorted(str(password)))) == password


def repeated_digit(password):
    str_password = str(password)
    return len(set(str_password)) < len(str_password)


def part_2_repeated_digit(password):
    str_password = str(password)
    unique_digits = set(str_password)
    return any(str_password.count(digit) == 2 for digit in unique_digits)


part_1_candidates = (
    password
    for password in range(lower_bound, upper_bound)
    if digits_increasing(password) and repeated_digit(password)
)
part_1 = sum(1 for _ in part_1_candidates)
print("Part 1:", part_1)

part_2_candidates = (
    password
    for password in range(lower_bound, upper_bound)
    if digits_increasing(password) and part_2_repeated_digit(password)
)
part_2 = sum(1 for _ in part_2_candidates)
print("Part 2:", part_2)

from itertools import tee

def fuel_required(mass):
    return (mass // 3) - 2

def part2_fuel(base_fuel):
    total_fuel = base_fuel
    d_fuel = fuel_required(base_fuel)
    while d_fuel > 0:
        total_fuel += d_fuel
        d_fuel = fuel_required(d_fuel)
    return total_fuel

with open('./1.in', 'r') as f:
    base_fuel, base_fuel_copy = tee(fuel_required(int(line)) for line in f)
    part_1 = sum(base_fuel)
    part_2 = sum(part2_fuel(fuel) for fuel in base_fuel_copy)
    print('Part 1:', part_1)
    print('Part 2:', part_2)

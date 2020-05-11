from intcode import load_program, run_program, run_nv_program


def find_target_output(program, target, search_depth):
    for noun in range(search_depth):
        for verb in range(search_depth):
            if run_nv_program(program, [], noun, verb) == target:
                return (noun, verb)


base_program = load_program("2.in")

# Part 1
part_1 = run_nv_program(base_program, [], 12, 2)

print("Part 1:", part_1)

# Part 2
noun, verb = find_target_output(base_program, 19690720, 100)
part_2 = 100 * noun + verb
print("Part 2:", part_2)

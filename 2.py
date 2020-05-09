def run_program(program):
    pc = 0
    alive = True
    while alive:
        if program[pc] == 1:
            op_1_loc = program[pc + 1]
            op_2_loc = program[pc + 2]
            store = program[pc + 3]
            program[store] = program[op_1_loc] + program[op_2_loc]
        elif program[pc] == 2:
            op_1_loc = program[pc + 1]
            op_2_loc = program[pc + 2]
            store = program[pc + 3]
            program[store] = program[op_1_loc] * program[op_2_loc]
        elif program[pc] == 99:
            alive = False
        else:
            raise Error()
        pc += 4

    # Value at address 0 is defined as the output
    return program[0]

def run_nv_program(program, noun, verb):
    modified_program = list(program)
    modified_program[1] = noun
    modified_program[2] = verb
    return run_program(modified_program)

def find_target_output(program, target, search_depth):
    for noun in range(search_depth):
        for verb in range(search_depth):
            if run_nv_program(program, noun, verb) == target:
                return (noun, verb)

base_program = None
with open('./2.in', 'r') as f:
    base_program = list(map(int, f.read().split(',')))

# Part 1
part_1 = run_nv_program(base_program, 12, 2)

print('Part 1:', part_1)

# Part 2
noun, verb = find_target_output(base_program, 19690720, 100)
part_2 = 100 * noun + verb
print('Part 2:', part_2)

class Terminate(Exception):
    pass


def terminate(_):
    raise Terminate()


def assign(program, loc, value):
    program[loc] = value


# op_code : (num_parameters, mode_overrides, consume_input, execute_callback)
# store location operands are ALWAYS immediate
INTCODE_ISA = {
    1: (
        3,
        [None, None, 1],
        False,
        lambda program, operand_1, operand_2, store: assign(
            program, store, operand_1 + operand_2
        ),
    ),
    2: (
        3,
        [None, None, 1],
        False,
        lambda program, operand_1, operand_2, store: assign(
            program, store, operand_1 * operand_2
        ),
    ),
    3: (1, [1], True, lambda program, stdin, store: assign(program, store, stdin)),
    4: (1, [None], True, lambda program, stdin, operand: print("DIAG", operand)),
    99: (0, [], False, terminate),
}


def get_operands(pc, num_operands, parameter_modes, program):
    # Fetch num_operands next slots in memory
    raw_operands = [program[pc + offset + 1] for offset in range(num_operands)]

    # Resolve operand values according to mode
    operands = [
        raw_operands[n] if parameter_modes[n] == 1 else program[raw_operands[n]]
        for n in range(num_operands)
    ]

    return operands


def resolve_operation(raw_op_code):
    raw_op_code = str(raw_op_code)

    # op_code is always the last 2 digits
    op_code = int(raw_op_code[-2:])
    num_operands, mode_overrides, _, _ = INTCODE_ISA[op_code]

    # Extract parameter modes from the raw operator
    raw_parameter_modes = list(
        map(
            int,
            list(
                # Pad with mode 0 to the right length
                "0" * (num_operands - (max(0, len(raw_op_code) - 2)))
                + raw_op_code[:-2]
            )[
                ::-1  # Parameter modes are read right to left
            ],
        )
    )

    # Apply mode overrides if present
    parameter_modes = [
        raw_parameter_modes[n] if mode_overrides[n] == None else mode_overrides[n]
        for n in range(num_operands)
    ]
    return (op_code, parameter_modes)


def run_program(program, stdin):
    try:
        pc = 0
        while True:
            op_code, parameter_modes = resolve_operation(program[pc])
            num_operands, _, consume_input, operator_callback = INTCODE_ISA[op_code]
            operands = get_operands(pc, num_operands, parameter_modes, program)

            # Spread the operands as separate arguments in the operator callback
            if consume_input:
                operator_callback(program, stdin[0], *operands)
            else:
                operator_callback(program, *operands)

            # Program counter advances by num_operands + 1 for the op_code
            pc += num_operands + 1
    except Terminate:
        pass

    # Value at address 0 is defined as the output
    return program[0]


def run_nv_program(program, stdin, noun, verb):
    modified_program = dict(program)
    modified_program[1] = noun
    modified_program[2] = verb
    return run_program(modified_program, stdin)


def load_program(filename):
    with open(filename, "r") as f:
        program = list(map(int, f.read().split(",")))
        return {addr: program[addr] for addr in range(len(program))}

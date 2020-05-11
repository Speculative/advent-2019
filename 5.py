from intcode import load_program, run_program

program = load_program("./5.in")
# stdin is defined as [1] in the problem
run_program(program, [1])

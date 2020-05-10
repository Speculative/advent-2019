# Turn is (direction, distance)[]
def get_turns(line):
    return ((turn[0], int(turn[1:])) for turn in line.split(","))


def move_by(start, direction, distance):
    if direction == "U":
        return (start[0], start[1] + distance)
    elif direction == "D":
        return (start[0], start[1] - distance)
    elif direction == "R":
        return (start[0] + distance, start[1])
    elif direction == "L":
        return (start[0] - distance, start[1])


def get_wire_trace(turns):
    trace = dict()
    loc = (0, 0)
    traveled = 0
    for direction, distance in turns:
        for step in range(distance):
            step_loc = move_by(loc, direction, step)
            if not (step_loc in trace):
                trace[step_loc] = traveled + step
        loc = move_by(loc, direction, distance)
        traveled += distance

    # explicitly remove the origin
    del trace[(0, 0)]
    return trace


def manhattan_distance(coord):
    return abs(coord[0]) + abs(coord[1])


def total_signal_delay(coord, wire_1_trace, wire_2_trace):
    return wire_1_trace[coord] + wire_2_trace[coord]


with open("./3.in", "r") as f:
    wire_1_turns = get_turns(f.readline())
    wire_2_turns = get_turns(f.readline())
    wire_1_trace = get_wire_trace(wire_1_turns)
    wire_2_trace = get_wire_trace(wire_2_turns)

    # Part 1
    wire_intersections = (set(wire_1_trace.keys())).intersection(
        set(wire_2_trace.keys())
    )
    intersection_distances = (
        manhattan_distance(intersection) for intersection in wire_intersections
    )
    closest_intersection = min(sorted(intersection_distances))
    print("Part 1:", closest_intersection)

    # Part 2
    intersection_signal_delays = (
        total_signal_delay(intersection, wire_1_trace, wire_2_trace)
        for intersection in wire_intersections
    )
    lowest_signal_delay_intersection = min(sorted(intersection_signal_delays))
    print("Part 2:", lowest_signal_delay_intersection)


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


def get_wire_occupied(turns):
    occupied = set()
    loc = (0, 0)
    for direction, distance in turns:
        occupied.update((move_by(loc, direction, step) for step in range(distance)))
        loc = move_by(loc, direction, distance)

    # explicitly ignore the origin
    occupied.remove((0, 0))
    return occupied


def manhattan_distance(coord):
    return abs(coord[0]) + abs(coord[1])


with open("./3.in", "r") as f:
    wire_1_turns = get_turns(f.readline())
    wire_2_turns = get_turns(f.readline())
    wire_1_occupied = get_wire_occupied(wire_1_turns)
    wire_2_occupied = get_wire_occupied(wire_2_turns)
    wire_intersections = wire_1_occupied.intersection(wire_2_occupied)
    intersection_distances = (
        manhattan_distance(intersection) for intersection in wire_intersections
    )
    closest_intersection = min(sorted(intersection_distances))
    print("Part 1:", closest_intersection)

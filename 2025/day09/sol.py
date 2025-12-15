def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [tuple(map(int, line.replace("\n","").split(","))) for line in lines]

    return lines

def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def partA(squares):
    rectangles = []
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            rectangles.append((i, j, area(squares[i], squares[j])))

    rectangles.sort(key=lambda x: x[2], reverse=True)

    return rectangles[0][2]

#raycast straight up (y+) and see how many horizontal lines were intersected
def raycast_count(p, lines):
    count = 0
    for start, end in lines:
        #check for a horizontal line, above the raycast point, and within the x coordinate
        if start[1] == end[1] \
            and start[1] > p[1] \
            and min(start[0], end[0]) <= p[0] <= max(start[0], end[0]):
            count += 1

        #debug
        '''
        print(f"raycast point {p}, line {(start, end)}")
        if not(start[1] == end[1]):
            print("not horizontal")
        elif not (start[1] > p[1]):
            print("not above")
        elif not (min(start[0], end[0]) <= p[0] <= max(start[0], end[0])):
            print("not between")
        else:
            print("hit")
        '''
            

    return count

def point_in_poly(p, lines):
    #odd number of crossings = inside,
    #even = outside
    return raycast_count(p, lines) % 2 == 1

def line_intersection(line1, line2):
    start_i, end_i = 0, 1
    x_i, y_i = 0, 1

    line1_horizontal = line1[start_i][y_i] == line1[end_i][y_i]
    line2_horizontal = line2[start_i][y_i] == line2[end_i][y_i]

    if line1_horizontal == line2_horizontal:
        return False
    
    if line1_horizontal:
        #x of line 2 is within x range of line 1
        #y of line 1 is within y range of line 2
        x_check = min(line1[start_i][x_i], line1[end_i][x_i]) <= line2[start_i][x_i] <= max(line1[start_i][x_i], line1[end_i][x_i])
        y_check = min(line2[start_i][y_i], line2[end_i][y_i]) <= line1[start_i][y_i] <= max(line2[start_i][y_i], line2[end_i][y_i])
    else:
        #swap lines 1 and 2 if line 2 is horizontal
        x_check = min(line2[start_i][x_i], line2[end_i][x_i]) <= line1[start_i][x_i] <= max(line2[start_i][x_i], line2[end_i][x_i])
        y_check = min(line1[start_i][y_i], line1[end_i][y_i]) <= line2[start_i][y_i] <= max(line1[start_i][y_i], line1[end_i][y_i])

    return x_check and y_check

def line_poly_intersection(line, poly):
    for p_line in poly:
        if line_intersection(line, p_line):
            return True
    return False

def poly_poly_edge_intersection(poly1, poly2):
    for p_line1 in poly1:
        for p_line2 in poly2:
            if line_intersection(p_line1, p_line2):
                return True
            
    return False

import matplotlib.pyplot as plt
def show_polygons(polygons):
    fig, ax = plt.subplots()

    colors = [
        'r', #red
        'k', #black
        'g', #green
        'b', #blue
        'c', #cyan
        'm', #magenta
        'y', #yellow
    ]

    for lines, color in zip(polygons, colors):

        #draw the starting point
        start_line = lines[0]
        start_point = start_line[0]
        plt.scatter([start_point[0]], [start_point[1]], marker='o', color=color)

        #draw the lines
        for start, end in lines:
            ax.annotate("", xytext=(start[0], start[1]), xy=(end[0], end[1]),
                arrowprops=dict(arrowstyle="->", color=color))
            
    #calculate the limits
    x_min = min(min(start[0], end[0]) for lines2 in polygons for start, end in lines2)
    x_max = max(max(start[0], end[0]) for lines2 in polygons for start, end in lines2)
    y_min = min(min(start[1], end[1]) for lines2 in polygons for start, end in lines2)
    y_max = max(max(start[1], end[1]) for lines2 in polygons for start, end in lines2)
        
    ax.set_xlim((x_min - 1, x_max + 1))
    ax.set_ylim((y_min - 1, y_max + 1))
    ax.grid(True)
    plt.show()
    
#Return the direction of a line in degrees. Only handles cardinal directions
# 0 is upwards (y positive)
def line_dir(line):
    start, end = line
    if start == end:
        assert False, "line of 0 length"

    if start[0] == end[0]: #vertical
        if start[1] < end[1]:
            return 0 #y+, up
        else:
            return 180 #y-, down
    elif start[1] == end[1]: #horizontal
        if start[0] < end[0]:
            return 90 #x+, right
        else:
            return 270 #x-, left
    else:
        assert False, "diagonal line, not currently handled"

def corner_angle(line1, line2):
    angle = line_dir(line2) - line_dir(line1)
    angle = (angle + 180) % 360 - 180 # constrain to -180 to +180 range
    return angle

#return a list of pairs of an element and its successor, wrapping around to 0 from the last element
#e.g. [1,2,3] -> [(1,2), (2,3), (3,1)]
def circular_zip(l):
    return list(zip(l, l[1:])) + [(l[-1], l[0])]

def count_turns(lines):
    rotation = 0
    pairs_of_lines = circular_zip(lines)
    for line1, line2 in pairs_of_lines:
        rotation += corner_angle(line1, line2)

    assert rotation % 360 == 0, "somehow, the total rotation is not a complete number of turns"

    return rotation // 360


def expand_lines(lines):

    turns = count_turns(lines)
    assert turns == 1 or turns == -1
    clockwise = turns == 1

    if clockwise != False:
        assert False, "case not programmed"

    #for shapes going counterclockwise:
    # expand lines going up:   move them to the right
    # expand lines going left: move them up
    for line_idx in range(len(lines)):
        line = lines[line_idx]
        if line_dir(line) == 0: #line going up, move to the right
            start, end = lines[line_idx]
            lines[line_idx] = ((start[0] + 1, start[1]), (end[0] + 1, end[1]))

            #adjust the line before and after too
            #Note: this maybe would have been simpler with points instead of lines, since they are shared between lines
            line_idx_next = (line_idx + 1) % len(lines)
            start, end = lines[line_idx_next]
            lines[line_idx_next] = ((start[0] + 1, start[1]), end)

            line_idx_prev = (line_idx - 1) % len(lines)
            start, end = lines[line_idx_prev]
            lines[line_idx_prev] = (start, (end[0] + 1, end[1]))

        elif line_dir(line) == 270: #line going left, move up
            start, end = lines[line_idx]
            lines[line_idx] = ((start[0], start[1] + 1), (end[0], end[1] + 1))

            #adjust the line before and after too
            line_idx_next = (line_idx + 1) % len(lines)
            start, end = lines[line_idx_next]
            lines[line_idx_next] = ((start[0], start[1] + 1), end)

            line_idx_prev = (line_idx - 1) % len(lines)
            start, end = lines[line_idx_prev]
            lines[line_idx_prev] = (start, (end[0], end[1] + 1))


def rectangle_from_corners(a, b):
    #counterclockwise
    #0 > 1
    #^   v
    #3 < 2

    #y+
    #^
    #0 > x+

    points = [
        (min(a[0], b[0]), min(a[1], b[1])),
        (max(a[0], b[0]), min(a[1], b[1])),
        (max(a[0], b[0]), max(a[1], b[1])),
        (min(a[0], b[0]), max(a[1], b[1])),
    ]

    points = [
        (points[0][0] + 0.50, points[0][1] + 0.50),
        (points[1][0] + 0.50, points[1][1] + 0.50),
        (points[2][0] + 0.50, points[2][1] + 0.50),
        (points[3][0] + 0.50, points[3][1] + 0.50)
    ]

    return points

def partB(points):
    polygon_lines = circular_zip(points)

    expanded_polygon_lines = list(polygon_lines)
    expand_lines(expanded_polygon_lines)

    rectangles = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            new_corners = rectangle_from_corners(points[i], points[j])
            #check each corner is inside polygon
            completely_inside = all(point_in_poly(corner, expanded_polygon_lines) for corner in new_corners)

            if(completely_inside):
                new_poly = circular_zip(new_corners)
                intersecting = poly_poly_edge_intersection(expanded_polygon_lines, new_poly)
                if not intersecting:
                    rectangles.append((i, j, area(points[i], points[j])))

        if(i % 20 == 0):
            print(f"{i}/{len(points)}")

    rectangles.sort(key=lambda x: x[2], reverse=True)

    solution = rectangles[0]

    print("B solution")
    print(solution)
    new_corners = rectangle_from_corners(points[solution[0]], points[solution[1]])
    show_polygons([
        expanded_polygon_lines,
        circular_zip(new_corners)
    ])

    return solution[2]

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 50

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 4774877510

    result = partB(parsedA_example)
    print(result)
    assert result == 24
    
    result = partB(parsedA)
    print(result)
    assert result == 1560475800


if __name__ == '__main__':
    main()
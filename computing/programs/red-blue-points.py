s = "dummy"
min_red_x = max_red_x = min_red_y = max_red_y = None
min_blue_x = max_blue_x = min_blue_y = max_blue_y = None

while True:
    s = input()
    if s == "":
        break
    x, y, colour = s.split()
    x = float(x)
    y = float(y)
    colour = colour.upper()
    match colour:
        case 'R':
            if min_red_x == None:
                min_red_x = max_red_x = x
            if min_red_x > x:
                min_red_x = x
            if max_red_x < x:
                max_red_x = x

            if min_red_y == None:
                min_red_y = max_red_y = y
            if min_red_y > y:
                min_red_y = y
            if max_red_y < y:
                max_red_y = y
        case 'B':
            if min_blue_x == None:
                min_blue_x = max_blue_x = x
            if min_blue_x > x:
                min_blue_x = x
            if max_blue_x < x:
                max_blue_x = x

            if min_blue_y == None:
                min_blue_y = max_blue_y = y
            if min_blue_y > y:
                min_blue_y = y
            if max_blue_y < y:
                max_blue_y = y

if max_red_x < min_blue_x or max_blue_x < min_red_x:
    print("Points can be separated by a line parallel to the Y axis")

if max_red_y < min_blue_y or max_blue_y < min_red_y:
    print("Points can be separated by a line parallel to the X axis")

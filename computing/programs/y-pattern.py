import sys


def print_y_pattern(stroke_width, gap, height):
    for i in range(gap//2 + 1):
        print(' '*i + 
              '#'*stroke_width + 
              ' '*(gap-2*i) + 
              '#'*stroke_width)

    for i in range(height-1):
        print(' '*(gap//2) + 
              '#'*(2*stroke_width))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit('Usage: %s <stroke-width> <gap> <stem height>' % sys.argv[0])

    stroke_width = int(sys.argv[1])
    gap = int(sys.argv[2])
    height = int(sys.argv[3])
    print_y_pattern(stroke_width, gap, height)

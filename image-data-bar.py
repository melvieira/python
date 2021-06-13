"""
Image Visualization Project.
"""
from simpleimage import SimpleImage

GREEN = 127
BLUE = 127
MAX_RED_VALUE = 255
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 200
height = 200
FILENAME = 'data-illiteracy.txt'

def main():
    floats_list = line()
    length = (len(floats_list))
    width = CANVAS_WIDTH * length
    start_x = 0
    start_y = 0
    new_canvas = SimpleImage.blank(width, height)
    for i in range(0, length):
        value = (floats_list[i])
        print(value)
        section = make_colored_section(value)
        new_canvas = put_section(new_canvas,section, start_x, start_y)
        start_x += 100
    new_canvas.show()

def line():
    """
    Create a list of the values. Assumes first two
    lines of file are the title
    and number of enteries and skips them.
    """
    f = open(FILENAME)
    next (f)
    next (f)
    floats_list = []
    for line in f:
        for line in line.split():
            floats_list.append(float(line))
    return floats_list

def make_colored_section(value):
    """
    Color a section based on the value from the data lsit.
    """
    section = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    width = section.width
    height = section.height

    for pixel in section:
        pixel.red = value * MAX_RED_VALUE
        pixel.blue = BLUE
        pixel.green = GREEN
    return section


def put_section(new_canvas,section, start_x, start_y):
    """
    Put the colored section on the new canvas.
    """
    width = section.width
    height = section.height
    for y in range (height):
        for x in range (width):
            pixel = section.get_pixel(x,y)
            new_canvas.set_pixel((start_x+x),(start_y+y),pixel)
    return new_canvas


if __name__ == '__main__':
    main()

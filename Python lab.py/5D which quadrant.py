'''Develop a function that accepts a point in a plane as an argument or arguments and returns 
a string. indicating in which quadrant the point lies, or if it lies on an axis or is the origin 
itself.'''

def quadrant(x, y):
    if x > 0 and y > 0:
        return "Lies in First quadrant"
    elif x < 0 and y > 0:
        return "Lies in Second quadrant"
    elif x < 0 and y < 0:
        return "Lies in Third quadrant"
    elif x > 0 and y < 0:
        return "Lies in Fourth quadrant"
    elif x == 0 and y > 0:
        return "Lies on the positive y-axis"
    elif x == 0 and y < 0:
        return "Lies on the negative y-axis"
    elif y == 0 and x < 0:
        return "Lies on the negative x-axis"
    elif y == 0 and x > 0:
        return "Lies on the positive x-axis"
    else:
        return "Lies at the origin"

# Input from the user
x = int(input('Enter x point: '))
y = int(input('Enter y point: '))

# Print the quadrant or axis information
print(quadrant(x, y))

# Example Output:
# (1) Enter x point: 1
#     Enter y point: 2
#     Lies in First quadrant
#
# (2) Enter x point: -1
#     Enter y point: 2
#     Lies in Second quadrant
#
# (3) Enter x point: -1
#     Enter y point: -2
#     Lies in Third quadrant
#
# (4) Enter x point: 1
#     Enter y point: -2
#     Lies in Fourth quadrant
#
# (5) Enter x point: 0
#     Enter y point: 2
#     Lies on the positive y-axis
#
# (6) Enter x point: 0
#     Enter y point: -2
#     Lies on the negative y-axis
#
# (7) Enter x point: 1
#     Enter y point: 0
#     Lies on the positive x-axis
#
# (8) Enter x point: -1
#     Enter y point: 0
#     Lies on the negative x-axis
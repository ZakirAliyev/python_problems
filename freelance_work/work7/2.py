"""
how to draw Star in PYTHON ?
"""

import turtle

# Starting a Working Screen
ws = turtle.Screen()

# initializing a turtle instance
t = turtle.Turtle()
t.fillcolor('yellow')
t.begin_fill()
# executing loop 5 times for a star
for i in range(5):
    # moving turtle 100 units forward
    t.forward(100)

    # rotating turtle 144 degree right
    t.right(144)

t.end_fill()

turtle.mainloop()
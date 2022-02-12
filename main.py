# import colorgram

# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(40, 178, 7), (87, 180, 248), (219, 111, 156), 
(146, 81, 6), (239, 119, 45), (11, 85, 211), (12, 60, 139), 
(215, 177, 115), (111, 234, 104), (249, 60, 249), (55, 70, 232), 
(184, 246, 179), (210, 11, 103), (40, 246, 35), (159, 235, 124), 
(241, 37, 45), (29, 144, 121), (190, 106, 41), (138, 5, 8), 
(82, 253, 247), (21, 101, 6), (10, 218, 209), (94, 
57, 9), (227, 202, 166), (213, 28, 121), (10, 49, 110)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
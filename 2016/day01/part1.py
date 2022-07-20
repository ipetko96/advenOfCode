import turtle

turtle.tracer(0, 0)
turtle.setheading(90)

with open("2016\\day01\\input", "r") as file:
    instructions = file.read().split(", ")
    for ins in instructions:
        if ins[:1] == "R":
            turtle.rt(90)
        else:
            turtle.lt(90)
        turtle.fd(int(ins[1:]))

    turtle.update()
    end = list(turtle.position())
    print(abs(round(end[0])) + abs(round(end[1])))

turtle.mainloop()

colors = ["blue", "green", "yellow"]

try:
    print(colors[3])
except IndexError:
    print("What?")

print(colors)

colors[2] = "red"

print(colors)
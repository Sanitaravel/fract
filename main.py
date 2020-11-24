import turtle
import svgwrite

size = 300
points = []


def koch_curve(size, n):
    points.append(turtle.pos())
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)


def main():
    n = int(input("Input iteration value: "))
    koch_curve(size, n)

    dwg = svgwrite.Drawing('koch.svg', profile='tiny')
    for i in range(len(points) - 1):
        a, b = points[i], points[i + 1]
        a[1] += 100
        b[1] += 100
        dwg.add(dwg.line(a, b, stroke=svgwrite.rgb(0, 0, 0, '%')))
    dwg.save()


if __name__ == '__main__':
    main()

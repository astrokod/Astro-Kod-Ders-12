import p5
import math

w, h = 500, 500
r = 225

def setup():
    p5.size(w, h)


def draw():
    p5.background(0)
    p5.translate(w/2, h/2)
    # p5.circle((0, 0), 50)

    for i in range(0, 360, 30):
        x = r * math.cos(math.radians(i))
        y = r * math.sin(math.radians(i))

        p5.fill(255, 0, 0)
        p5.no_stroke()
        p5.circle((x, y), 15)


    for u in range(0, 360, 6):
        if u % 30:
            x = r * math.cos(math.radians(u))
            y = r * math.sin(math.radians(u))

            p5.fill(255)
            p5.no_stroke()
            p5.circle((x, y), 10)



if __name__ == "__main__":
    p5.run()

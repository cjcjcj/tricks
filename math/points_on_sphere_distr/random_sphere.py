import math
import random


def get_onsphere_point(r):
    theta = random.uniform(0, math.pi*2)
    u = random.uniform(-1., 1.)
    a = math.sqrt(1. - u*u)

    point = (
        r * math.cos(theta) * a,
        r * math.sin(theta) * a,
        r * u
    )

    return point


def get_sphere_points_population(n, r):
    for i in range(n):
        yield get_onsphere_point(r)


if __name__ == '__main__':
    n = 1500
    r = 4000
    points = list(get_sphere_points_population(n, r))

import matplotlib.pyplot as plt
import numpy as np

def calculate_y_on_separator(x: float) -> float:
    # The line equation developed in the preparatory assignment, to seperate points evenly
    # Returns the y-value on the separating line for a given x-value.
    return -0.725 * x + 0.475


def f(x):
    return -0.489*x


def g(x):
    return -2*x + 0.16


def h(x):
    return 800*x - 120


def classify_data(points, function):
    red_points = []
    blue_points = []

    for point in points:
        x, y = point

        # is_positive_x = function(x+1) > function(x)

        # if is_positive_x:
        #     label = 0 if y > function(x) else 1
        # else: 
        #     label = 1 if y > function(x) else 0

        label = 1 if y > function(x) else 0

        if label == 1:
            blue_points.append(point)
        else:
            red_points.append(point)

    return red_points, blue_points


def scatter_classified_point_and_line_for_function(points, f, title=None):
    red, blue = classify_data(points, f)

    min_axis = -6
    max_axis = 6

    X = np.linspace(min_axis, max_axis)

    fig, ax = plt.figure(dpi=100), plt.axes()

    if title != None:
        ax.set(title=title)
        
    ax.set_xlim((min_axis, max_axis))
    ax.set_ylim((min_axis, max_axis))

    ax.plot(X, [f(x) for x in X])
    ax.scatter([p[0] for p in red], [p[1] for p in red], alpha=0.6, c="red")
    ax.scatter([p[0] for p in blue], [p[1] for p in blue], alpha=0.6, c="blue")
    plt.show()

    print(f"Antal röda: {len(red)}")
    print(f"Antal blåa: {len(blue)}")


def get_unlabelled_points():
    points = []

    with open("Data/unlabelled_data.csv", "r") as file:
        for line in file:
            x, y = [float(v.strip()) for v in line.split(",")]
            point = (x, y)
            points.append(point)
    
    return points
# This file contains functions used in the main script and in the report.
# It does not execute any code by itself.

from typing import Callable

def calculate_y_on_separator(x: float) -> float:
    # The line equation developed in the preparatory assignment, to seperate points evenly.
    # Returns the y-value on the separating line for a given x-value.
    return -0.725 * x + 0.475


def f(x: float) -> float:
    return -0.489*x


def g(x: float) -> float:
    return -2*x + 0.16


def h(x: float) -> float:
    return 800*x - 120


def get_classification_label_for_point(point: tuple, f: Callable) -> int:
    x, y = point

    # Returns 1 if the y-value of the point is greater than the y-value of the separating line at the same x-coordinate, meaning the point is above the line. Otherwise, returns 0.
    return 1 if y > f(x) else 0
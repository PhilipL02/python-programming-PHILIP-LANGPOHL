import matplotlib.pyplot as plt
import numpy as np
from typing import Callable
from lab3_utils import calculate_y_on_separator, get_classification_label_for_point

# Constants (Global variables that should not be changed)
PATH_TO_DATA_FOLDER = "Labs/Lab3/Data"


# The function here can be changed if points should be classified and plotted with other function
function_for_classification = calculate_y_on_separator


def classify_unlabelled_data(f: Callable) -> None:
    # Open both the file with unlabelled data, and the new file that will contain labelled data.
    # Both opens here in order to only use one loop, both for reading and writing.
    with open(f"{PATH_TO_DATA_FOLDER}/unlabelled_data.csv", "r") as file_read, open(f"{PATH_TO_DATA_FOLDER}/labelled_data.csv", "w") as file_write:
        for line in file_read:
            x, y = [float(v.strip()) for v in line.split(",")] # Get values for x and y as floats from the line
            label = get_classification_label_for_point((x, y), f)

            file_write.write(f"{x},{y},{label}\n") # Write the line to the new file, including the classified label


def plot_line_and_classified_data_points(f: Callable) -> None:
    red_points = []
    blue_points = []

    with open(f"{PATH_TO_DATA_FOLDER}/unlabelled_data.csv", "r") as file_read:
        for line in file_read:
            x, y = [float(v.strip()) for v in line.split(",")] # Get values for x and y as floats from the line
            point = (x, y)
            label = get_classification_label_for_point(point, f)

            # Seperate the points by the label to two different lists
            if label == 1:
                blue_points.append(point)
            else:
                red_points.append(point)


    fig, ax = plt.figure(dpi=100), plt.axes()

    X = np.linspace(-6, 6)

    # Plot the line in the graph
    ax.plot(X, [f(x) for x in X])

    # Scatter the classified points with color differenting the classes
    ax.scatter([p[0] for p in red_points], [p[1] for p in red_points], alpha=0.6, c="red")
    ax.scatter([p[0] for p in blue_points], [p[1] for p in blue_points], alpha=0.6, c="blue")
    
    ax.set_xlim((-6, 6))
    ax.set_ylim((-6, 6))

    plt.show()


# Call the function that will read unlabelled data, and write the labelled data to labelled_data.csv
classify_unlabelled_data(function_for_classification)

# Call the function that will read unlabelled data, and plot the line and classified points in a graph
plot_line_and_classified_data_points(function_for_classification)

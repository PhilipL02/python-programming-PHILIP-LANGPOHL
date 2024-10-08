import matplotlib.pyplot as plt
import numpy as np

# Constants
PATH_TO_DATA_FOLDER = "Labs/Lab3/Data"

def calculate_y_on_separator(x: float) -> float:
    # The line equation developed in the preparatory assignment, to seperate points evenly
    # Returns the y-value on the separating line for a given x-value.
    return -0.725 * x + 0.475


def get_classification_label_for_point(point: tuple) -> int:
    x, y = point

    # Returns 1 if the y-value of the point is greater than the y-value of the separating line at the same x-coordinate, meaning the point is above the line. Otherwise, returns 0.
    return 1 if y > calculate_y_on_separator(x) else 0


def classify_unlabelled_data() -> None:
    # Open both the file with unlabelled data, and the new file that will contain labelled data
    with open(f"{PATH_TO_DATA_FOLDER}/unlabelled_data.csv", "r") as file_read, open(f"{PATH_TO_DATA_FOLDER}/labelled_data.csv", "w") as file_write:
        for line in file_read:
            x, y = [float(v.strip()) for v in line.split(",")] # Get values for x and y as floats from the line
            label = get_classification_label_for_point((x, y))

            file_write.write(f"{x},{y},{label}\n") # Write the line to the new file, including the classified label


classify_unlabelled_data()

def plot_line_and_classified_data_points():
    red_points = []
    blue_points = []

    with open(f"{PATH_TO_DATA_FOLDER}/unlabelled_data.csv", "r") as file_read:
        for line in file_read:
            x, y = [float(v.strip()) for v in line.split(",")] # Get values for x and y as floats from the line
            p = (x, y)
            label = get_classification_label_for_point(p)

            if label == 1:
                blue_points.append(p)
            else:
                red_points.append(p)

    fig, ax = plt.figure(dpi=100), plt.axes()
    X = np.linspace(-6, 6)

    ax.plot(X, [calculate_y_on_separator(x) for x in X])
    ax.scatter([p[0] for p in red_points], [p[1] for p in red_points], alpha=0.6, c="red")
    ax.scatter([p[0] for p in blue_points], [p[1] for p in blue_points], alpha=0.6, c="blue")
    plt.show()


plot_line_and_classified_data_points()

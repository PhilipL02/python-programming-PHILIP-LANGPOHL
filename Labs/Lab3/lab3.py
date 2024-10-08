def calculate_y_on_separator(x: float) -> float:
    # The line equation developed in the preparatory assignment, to seperate points evenly
    # Returns the y-value on the separating line for a given x-value.
    return -0.725 * x + 0.475


def get_classification_label_for_point(point: tuple) -> int:
    x, y = point

    # Returns 1 if the y-value of the point is greater than the y-value of the separating line at the same x-coordinate, meaning the point is above the line. Otherwise, returns 0.
    return 1 if y > calculate_y_on_separator(x) else 0


def classify_unlabelled_data() -> None:
    path_to_data_folder = "Labs/Lab3/Data"

    # Open both the file with unlabelled data, and the new file that will contain labelled data
    with open(f"{path_to_data_folder}/unlabelled_data.csv", "r") as file_read, open(f"{path_to_data_folder}/labelled_data.csv", "w") as file_write:
        for line in file_read:
            x, y = [float(v.strip()) for v in line.split(",")] # Get values for x and y as floats from the line
            label = get_classification_label_for_point((x, y))

            file_write.write(f"{x},{y},{label}\n") # Write the line to the new file, including the classified label


classify_unlabelled_data()
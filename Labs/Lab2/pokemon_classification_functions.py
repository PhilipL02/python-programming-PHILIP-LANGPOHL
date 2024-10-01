import matplotlib.pyplot as plt
import numpy as np
import random
import os.path

def check_path_exists(path):
    return os.path.exists(path)


def get_datapoints() -> list:
    file_name = "datapoints.txt"
    if not check_path_exists(file_name):
        file_name = "Labs/Lab2/" + file_name

    # Initialize empty list
    datapoints = []

    with open(file_name, "r") as file:
        for line in file:
            if not line[0].isdigit(): # Ignore row if first character is not digit. (This ignores header row)
                continue

            # Get the values for width, height, label from the line
            width, height, label = [value.strip() for value in line.split(",")]

            # Format the values to correct type
            width = float(width)
            height = float(height)
            label = int(label)

            # Append dictonary of datapoint to the list of points
            datapoints.append({ "width": width, "height": height, "label": label })

    # Return the full list of datapoints collected from the file
    return datapoints


def get_testpoints() -> list:
    file_name = "testpoints.txt"
    if not check_path_exists(file_name):
        file_name = "Labs/Lab2/" + file_name

    # Initialize empty list
    testpoints = []

    with open(file_name, "r") as file:
        for line in file:
            if not line[0].isdigit(): # Ignore row if first character is not digit. (This ignores header row)
                continue
            
            point = line.split("(")[1].split(")")[0] # Get the point inside the parentheses

            # Get the values for width and height, and format as float
            width, height = [float(value) for value in point.split(",")]
            
            # Append dictonary of datapoint to the list of points
            testpoints.append({ "width": width, "height": height })
    
    # Return the full list of testpoints collected from the file
    return testpoints


def scatter_plot_datapoints(datapoints) -> None:
    fig, ax = plt.figure(dpi=100), plt.axes()

    pikachus = [d for d in datapoints if d["label"] == 1]
    pichus = [d for d in datapoints if d["label"] == 0]


    ax.scatter([d["width"] for d in pikachus], [d["height"] for d in pikachus], alpha=0.5, c="blue")
    ax.scatter([d["width"] for d in pichus], [d["height"] for d in pichus], alpha=0.5, c="red")
    ax.set(xlabel="Width (cm)", ylabel="Height (cm)", title="Height and width for pokemons")
    ax.legend(("Pikachu", "Pichu"))
    plt.show()


def get_distance_between_points(P1: tuple, P2: tuple) -> float:
    x1, y1 = P1
    x2, y2 = P2
    
    return np.sqrt((np.square(x2 - x1) + np.square(y2 - y1)))


def classify_testpoint(point: tuple, datapoints: list) -> str:
    closest_point = None
    for datapoint in datapoints:
        P2 = (datapoint["width"], datapoint["height"])
        distance = get_distance_between_points(point, P2)
        if not closest_point or distance < closest_point["distance"]:
            closest_point = { "distance": distance, "label": datapoint["label"] }
    
    return None if not closest_point else "Pikachu" if closest_point["label"] == 1 else "Pichu"


def output_classification_for_testpoints(testpoints: list, datapoints: list) -> None:
    for testpoint in testpoints:
        point = (testpoint["width"], testpoint["height"])
        
        classification = classify_testpoint(point, datapoints)

        print(f"Sample with (width, height): {point} classified as {classification}")


def split_source_data_into_training_and_test(source_data: list) -> tuple:
    random.shuffle(source_data)

    pikachu_data = []
    pichu_data = []
    for datapoint in source_data:
        if datapoint["label"] == 1:
            pikachu_data.append(datapoint)
        elif datapoint["label"] == 0:
            pichu_data.append(datapoint)

    train_data, test_data = pikachu_data[:50] + pichu_data[:50], pikachu_data[50:75] + pichu_data[50:75]

    random.shuffle(train_data)
    random.shuffle(test_data)

    return (train_data, test_data)


def get_user_input_pokemon_height():
    while True:
        height = input("Input the height of the pokemon: ")
        try:
            height = float(height)
            if height < 0:
                print("Height of the pokemon cannot be negative")
                continue

        except ValueError as err:
            print("Height of the pokemon must be a number")
            continue

        return height


def get_user_input_pokemon_width():
    while True:
        width = input("Input the width of the pokemon: ")
        try:
            width = float(width)
            if width < 0:
                print("Width of the pokemon cannot be negative")
                continue

        except ValueError as err:
            print("Width of the pokemon must be a number")
            continue

        return width


def get_k_nearest_neighbors(P1, points, k):
    sorted_by_distance = sorted(points, key=lambda point: get_distance_between_points(P1, (point["width"], point["height"])))
    return sorted_by_distance[:k]


def get_accuracy_from_random_data_split():
    source_data = get_datapoints()

    training_points, test_points = split_source_data_into_training_and_test(source_data)

    number_of_TP = 0
    number_of_TN = 0
    total_number = 0

    for test in test_points:
        point = (test["width"], test["height"])

        # The exercise said to use the 10 closest points, but I chose 9 to avoid equal split in the classification (5 Pichu, 5 Pikachu)
        closest_datapoints = get_k_nearest_neighbors(point, training_points, k=9)

        amount_pikachu = 0
        amount_pichu = 0
        for close_point in closest_datapoints:
            if close_point["label"] == 1:
                amount_pikachu += 1
            elif close_point["label"] == 0:
                amount_pichu += 1

        guessed_label = None if amount_pikachu == amount_pichu else 1 if amount_pikachu > amount_pichu else 0
        correct_label = test["label"]

        total_number += 1
        if guessed_label == 1 and correct_label == 1:
            number_of_TP += 1
        elif guessed_label == 0 and correct_label == 0:
            number_of_TN += 1

    accuracy = (number_of_TP + number_of_TN) / total_number

    return accuracy
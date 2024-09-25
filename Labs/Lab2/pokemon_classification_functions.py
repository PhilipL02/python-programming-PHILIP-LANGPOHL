import matplotlib.pyplot as plt
import numpy as np

def get_datapoints() -> list:
    path = "datapoints.txt"
    datapoints = []

    with open(path, 'r') as file:
        for line in file:
            if not line[0].isdigit(): # Ignore row if first character is not digit. (This ignores header row)
                continue

            width, height, label = [value.strip() for value in line.split(',')]
            width = float(width)
            height = float(height)
            label = int(label)

            entry = { "width": width, "height": height, "label": label }
            datapoints.append(entry)

    return datapoints


def get_testpoints() -> list:
    path = "testpoints.txt"
    testpoints = []

    with open(path, 'r') as file:
        for line in file:
            if not line[0].isdigit(): # Ignore row if first character is not digit. (This ignores header row)
                continue
            
            point = line.split('(')[1].split(')')[0] # Get the point inside the parentheses
            width, height = [float(value) for value in point.split(',')]
            
            entry = { "width": width, "height": height }
            testpoints.append(entry)
    
    return testpoints


def plot_datapoints(datapoints) -> None:
    for d in datapoints:
        x, y, is_pikachu = d["width"], d["height"], d["label"] == 1

        color = "red"
        if is_pikachu:
            color = "blue"

        plt.scatter(x, y, color=color)

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
    
    return None if not closest_point else 'Pikachu' if closest_point["label"] == 1 else 'Pichu'


def output_classification_for_testpoints(testpoints: list, datapoints: list) -> None:
    for testpoint in testpoints:
        point = (testpoint["width"], testpoint["height"])
        
        classification = classify_testpoint(point, datapoints)

        print(f"Sample with (width, height): {point} classified as {classification}")
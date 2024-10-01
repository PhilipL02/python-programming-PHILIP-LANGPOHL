from pokemon_classification_functions import get_datapoints, get_testpoints, scatter_plot_datapoints, output_classification_for_testpoints, get_user_input_pokemon_height, get_user_input_pokemon_width, get_k_nearest_neighbors, get_accuracy_from_random_data_split
import matplotlib.pyplot as plt

datapoints = get_datapoints()
scatter_plot_datapoints(datapoints)

testpoints = get_testpoints()
output_classification_for_testpoints(testpoints, datapoints)

# Let user input height and weight and create point of input values
user_pokemon_height = get_user_input_pokemon_height()
user_pokemon_width = get_user_input_pokemon_width()
user_point = (user_pokemon_height, user_pokemon_width)

# The exercise said to use the 10 closest points, but I chose 9 to avoid equal split in the classification (5 Pichu, 5 Pikachu)
nearest_neighbors = get_k_nearest_neighbors(user_point, datapoints, k=9)

# Loop the neighbors to get the amount of Pikachus and Pichus
amount_pikachu = 0
amount_pichu = 0
for neighbor in nearest_neighbors:
    if neighbor["label"] == 1:
        amount_pikachu += 1
    elif neighbor["label"] == 0:
        amount_pichu += 1

classification = "Pikachu" if amount_pikachu > amount_pichu else "Pichu"
print(f"Sample with (width, height): {user_point} classified as {classification}")

# TODO:
# Försök måla upp en matris för TP, FP med mera.

amount_of_attempts = 10
attempts_indexes = range(amount_of_attempts)
accuracies = [get_accuracy_from_random_data_split() for _ in attempts_indexes]
average_accuracy = sum(accuracies) / len(accuracies)

fig, ax = plt.figure(dpi=100), plt.axes()
ax.plot(attempts_indexes, accuracies)
ax.set(xlabel="Attempt", ylabel="Accuracy", title="Accuracy for multiple attempts")
plt.show()

print(f"Average accuracy is {average_accuracy:.2f}")

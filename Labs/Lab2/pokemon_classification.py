# This is the main script of the project.
# Run this file to perform classification and generate results.

from pokemon_classification_utils import get_datapoints, get_testpoints, scatter_plot_datapoints, output_classification_for_testpoints, get_user_input_pokemon_height, get_user_input_pokemon_width, get_classified_label_by_k_nearest_neighbors, get_accuracy_from_random_data_split, PIKACHU_LABEL
import matplotlib.pyplot as plt

datapoints = get_datapoints()
scatter_plot_datapoints(datapoints)

testpoints = get_testpoints()
output_classification_for_testpoints(testpoints, datapoints)

# Let user input height and weight and create point of input values
user_pokemon_width = get_user_input_pokemon_width()
user_pokemon_height = get_user_input_pokemon_height()
user_point = (user_pokemon_width, user_pokemon_height)

# The exercise said to use the 10 closest points, but I chose 9 to avoid equal split in the classification (5 Pichu, 5 Pikachu)
classified_label = get_classified_label_by_k_nearest_neighbors(user_point, datapoints, k=9)
classification = "Pikachu" if classified_label == PIKACHU_LABEL else "Pichu"
print(f"Your pokemon with (width, height): {user_point} classified as {classification}")

# Test model with multiple attempts, get the accuracies and calculate average accuracy
amount_of_attempts = 10
attempts_indexes = range(amount_of_attempts)
accuracies = [get_accuracy_from_random_data_split() for _ in attempts_indexes]
average_accuracy = sum(accuracies) / len(accuracies)

fig, ax = plt.figure(dpi=100, num="Accuracy for multiple attempts"), plt.axes()
ax.plot(attempts_indexes, accuracies)
ax.plot(attempts_indexes, [average_accuracy]*len(attempts_indexes), label='Mean', linestyle='--')
ax.set(xlabel="Attempt", ylabel="Accuracy", title="Accuracy for multiple attempts")
ax.legend(loc='upper right')

plt.show()

print(f"The average accuracy is around {average_accuracy:.2f}")

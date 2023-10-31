import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def get_accuracy(model, X_test, y_test, set_of_numbers):
    predicted_numbers = model.predict(X_test)
    score = model.score(X_test, y_test)

    # Filter the elements in the array that are in the list of numbers
    result = np.in1d(predicted_numbers, set_of_numbers)

    print(f"Model accuracy: {score}")

    if np.all(result):  # If all element of set_of_numbers in predicted_numbers
        return np.array(set_of_numbers)
    else:
        return None


dataset = [
    [14, 22, 32, 37, 43, 48, 42],
    [12, 20, 26, 33, 40, 44, 24],
    [11, 16, 24, 34, 47, 52, 15],
    [1, 23, 29, 37, 51, 55, 54],
    [13, 22, 33, 41, 46, 47, 9],
    [8, 23, 30, 34, 38, 47, 10],
    [5, 8, 9, 20, 36, 50, 35],
    [6, 23, 26, 37, 44, 46, 33],
    [4, 13, 36, 40, 43, 52, 34],
    [14, 22, 32, 37, 43, 48, 42],
    [12, 20, 26, 33, 40, 44, 24],
    [11, 16, 24, 34, 47, 52, 15],
    [1, 23, 29, 37, 51, 55, 54],
    [13, 22, 33, 41, 46, 47, 9],
    [8, 23, 30, 34, 38, 47, 10],
    [5, 8, 9, 20, 36, 50, 35],
    [6, 23, 26, 37, 44, 46, 33],
    [4, 13, 36, 40, 43, 52, 34],
    [1, 21, 33, 46, 47, 53, 9],
    # Add more data...
    # [11, 14, 25, 44, 46, 47, 10],
]
flattened_dataset = np.array(dataset).flatten()
reshaped_dataset = flattened_dataset.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(reshaped_dataset, reshaped_dataset, test_size=0.2,
                                                    random_state=None)

model = LinearRegression()
model.fit(X_train, y_train)

set_of_numbers = np.array([11, 14, 25, 44, 46, 47, 10])

# Get the accuracy of the model and filter the numbers if necessary
filtered_numbers = get_accuracy(model, X_test, y_test, set_of_numbers)
while True:

    if filtered_numbers is not None:
        print(f"Filtered numbers: {filtered_numbers}")
        break
    else:
        # Re-run the program
        import sys
        sys.stdout.flush()
        X_train, X_test, y_train, y_test = train_test_split(reshaped_dataset, reshaped_dataset, test_size=0.2, random_state=None)
        predicted_numbers = model.predict(X_test)

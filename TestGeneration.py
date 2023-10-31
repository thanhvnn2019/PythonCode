import numpy as np
from pandas.core.common import random_state
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

X_train, X_test, y_train, y_test = train_test_split(reshaped_dataset, reshaped_dataset, test_size=0.2, random_state=None)

model = LinearRegression()
model.fit(X_train, y_train)

# Given list
set_of_numbers = np.array([11, 14, 25, 44, 46, 47, 10])

score = model.score(X_test, y_test)
print(f"Model accuracy: {score}")

predicted_numbers = model.predict(X_test)

while True:
    # Use a list comprehension to filter the elements in the array that are in the list of numbers
    result = np.in1d(predicted_numbers, set_of_numbers)

    # Print the elements that are in the array
    if all(result):
        print(random_state)
        print(result)
        break
    else:
        print("Not all elements of the result array are true.")
        # Re-run the program
        import sys
        sys.stdout.flush()
        model.fit(X_train, y_train)
        predicted_numbers = model.predict(X_test)

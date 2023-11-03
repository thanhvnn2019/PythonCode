import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# Load the dataset
with open('D:\previous_results.txt', 'r') as file:
    data = pd.read_csv(file, delimiter=' ', header=0)

# Rename the columns
data.columns = ['Number', 'Number1', 'Number2', 'Number3', 'Number4', 'Number5', 'Number6']

# Define the feature set (X) and the target variable (y)
X = data[['Number1', 'Number2']]
y = data['Number']

# Scale the data
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y.values.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential()
model.add(Dense(32, input_dim=2, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=0)

# Make predictions using the testing data
predictions = model.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, predictions)
print('Mean Squared Error:', mse)

# Predict the next 6-number lottery result for each of the 10 possible digits
predictions = []
for i in range(10):
    for j in range(10):
        predictions.append(model.predict([[i, j]]))

# Find the most likely digit combinations
top_predictions = sorted(predictions, key=lambda x: x[0])[-6:]

# Combine the most likely digit combinations into a 6-number lottery result
next_result = ''
for prediction in top_predictions:
    next_result += str(int(prediction[0]))

print('Next 6-Number Lottery Result:', next_result)

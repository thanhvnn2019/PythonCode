import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.optimizers import Adam

# The sequence of 6-digit numbers
sequence = np.array([9, 15, 17, 21, 26, 36])

# Convert the sequence into a suitable input/output format for the RNN model
X = sequence[:-1].reshape(-1, 1)
y = sequence[1:].reshape(-1, 1)

# Build the RNN model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(1, 1)))
model.add(Dense(1))
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Train the model
model.fit(X, y, epochs=300, verbose=0)

# Use the trained model to predict the next 6-digit number sequence
input_seq = np.array([9, 15, 17, 21, 26, 36]).reshape(-1, 1)
predicted_seq = model.predict(input_seq)
predicted_seq = np.round(predicted_seq).astype(int)

print("Predicted 6-digit number sequence: ", predicted_seq)

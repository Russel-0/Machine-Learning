import numpy as np
from sklearn.linear_model import LinearRegression

user_input = input("Enter a sequence of numbers separated by spaces: ")
user_sequence = [float(num) for num in user_input.split()]

X = np.array([[i] for i in range(1, len(user_sequence) + 1)])
y = np.array(user_sequence)

model = LinearRegression()
model.fit(X, y)

next_number = model.predict([[len(user_sequence) + 1]])

print(f"Predicted next number in the sequence: {next_number[0]}")

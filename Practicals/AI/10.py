import numpy as np
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1)
        
        
    def activation_function(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        z = np.dot(x, self.weights[1:]) + self.weights[0]
        return self.activation_function(z)
    
    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                self.weights[1:] += self.learning_rate * error * X[i]
                self.weights[0] += self.learning_rate * error

if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Input features
    y = np.array([0, 1, 1, 1]) # Expected output (OR gate)
    perceptron = Perceptron(input_size=2)
    perceptron.train(X, y)
    for x in X:
        print(f"Input: {x}, Predicted Output: {perceptron.predict(x)}")
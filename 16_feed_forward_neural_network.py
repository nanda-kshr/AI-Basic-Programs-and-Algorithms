import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        # Forward propagation
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        
        return self.a2
    
    def backward(self, X, y, output, learning_rate):
        # Backpropagation
        m = X.shape[0]
        
        # Output layer error
        dz2 = output - y
        
        # Hidden layer gradients
        dW2 = np.dot(self.a1.T, dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        
        # Hidden layer error
        dz1 = np.dot(dz2, self.W2.T) * self.sigmoid_derivative(self.a1)
        
        # Input layer gradients
        dW1 = np.dot(X.T, dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        
        # Update weights
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
    
    def train(self, X, y, epochs, learning_rate):
        for i in range(epochs):
            # Forward propagation
            output = self.forward(X)
            
            # Backpropagation
            self.backward(X, y, output, learning_rate)
            
            # Calculate loss
            if i % 100 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {i}, Loss: {loss}")

# Example usage: XOR problem
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create and train the neural network
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)
nn.train(X, y, epochs=1000, learning_rate=0.1)

# Test the model
predictions = nn.forward(X)
print("\nPredictions:")
for i in range(len(X)):
    print(f"Input: {X[i]}, Predicted: {predictions[i][0]:.4f}, Actual: {y[i][0]}")
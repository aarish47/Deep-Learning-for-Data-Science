# **Types of Activation Functions**

## **Written by:** Aarish Asif Khan

## **Date:** 2 March 2024

## **Types of Activation Functions**

Activation functions play a crucial role in artificial neural networks by introducing non-linearity into the network's output. Here are some commonly used activation functions:

## 1. **ReLU (Rectified Linear Unit)**

- **Formula**: $f(x) = \max(0, x)$
- **Range**: [0, +∞)
- **Advantages**: Simple and computationally efficient, avoids vanishing gradient problem for positive inputs, encourages sparse activations.

## 2. **Sigmoid**

- **Formula**: $f(x) = \frac{1}{1 + e^{-x}}$
- **Range**: (0, 1)
- **Advantages**: Smooth and bounded, suitable for binary classification tasks where outputs need to be interpreted as probabilities.

## 3. **Tanh (Hyperbolic Tangent)**

- **Formula**: $f(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$
- **Range**: (-1, 1)
- **Advantages**: Similar to the sigmoid function but with outputs centered around zero, often used in hidden layers of neural networks.

## 4. **Softmax**

- **Formula**: $f(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{N} e^{x_j}}$ for $i = 1, 2, ..., N$
- **Range**: [0, 1] (each output is a probability)
- **Advantages**: Used in the output layer of multi-class classification tasks to produce a probability distribution over the classes.

## 5. **Leaky ReLU**

- **Formula**: $f(x) = \begin{cases} x, & \text{if } x > 0 \\ \text{leaky\_slope} \times x, & \text{otherwise} \end{cases}$
- **Range**: (-∞, +∞)
- **Advantages**: Addresses the "dying ReLU" problem by allowing a small gradient when the input is negative.

## 6. **ELU (Exponential Linear Unit)**

- **Formula**: $f(x) = \begin{cases} x, & \text{if } x > 0 \\ \alpha \times (e^{x} - 1), & \text{otherwise} \end{cases}$
- **Range**: (-α, +∞)
- **Advantages**: Similar to ReLU but with negative values, can lead to faster learning.

## 7. **Swish**

- **Formula**: $f(x) = \frac{x}{1 + e^{-x}}$
- **Range**: (-∞, +∞)
- **Advantages**: Similar to ReLU but with a smooth gradient, proposed to perform better than ReLU in some cases.

## 8. **GELU (Gaussian Error Linear Unit)**

- **Formula**: $f(x) = x \times \Phi(x)$, where $\Phi(x)$ is the cumulative distribution function of the standard normal distribution.
- **Range**: (-∞, +∞)
- **Advantages**: Smooth approximation of ReLU with non-zero mean, shown to improve performance in certain scenarios.

These activation functions serve different purposes and may be chosen based on the specific requirements of the neural network architecture and the nature of the task being addressed.

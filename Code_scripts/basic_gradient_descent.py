# The gradient descent algorithm will find the minimum of the
# f(x) = x^4 -3x^3 + 2
#f'(x) = 4x^3 - 9x^2
next_x = 7.85
gamma = 0.01 # The Step size multiplier

precision = 0.0001 # Desired precision of result
max_iters = 1000 # Maximum number of iterations

# Derivative function
df = lambda x: 4*x**3 -9*x**2

for i in range(max_iters):
    current_x = next_x
    next_x = current_x - gamma * df(current_x)
    step = next_x - current_x
    if abs(step) <= precision:
        break

print("minimum at", next_x)


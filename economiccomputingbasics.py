import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from statsmodels.api import OLS, add_constant
import pandas as pd

# 1. Utility Maximization
def utility_maximization():
    print("1. Utility Maximization")
    # Example utility function: U(x, y) = x^0.5 * y^0.5
    def utility_function(vars):
        x, y = vars
        return -(x ** 0.5 * y ** 0.5)  # Negative for maximization with minimize

    # Budget constraint: p1*x + p2*y = I
    p1, p2, I = 2, 3, 100  # Prices and income
    cons = [{'type': 'ineq', 'fun': lambda vars: I - (p1 * vars[0] + p2 * vars[1])},  # Budget
            {'type': 'ineq', 'fun': lambda vars: vars[0]},  # x >= 0
            {'type': 'ineq', 'fun': lambda vars: vars[1]}]  # y >= 0

    result = minimize(utility_function, [1, 1], constraints=cons)
    print("Optimal bundle: x =", result.x[0], ", y =", result.x[1])
    print("Maximum utility:", -result.fun)
    print()

# 2. Demand Curve Estimation
def demand_curve_estimation():
    print("2. Demand Curve Estimation")
    # Generate synthetic data
    np.random.seed(42)
    price = np.linspace(1, 10, 100)
    quantity = 100 - 2 * price + np.random.normal(0, 5, size=100)

    # Fit a linear demand curve: Q = a + bP
    X = add_constant(price)
    model = OLS(quantity, X).fit()
    print(model.summary())
    print()

    # Plot the demand curve
    plt.scatter(price, quantity, label="Data", alpha=0.6)
    plt.plot(price, model.predict(X), color="red", label="Fitted Demand Curve")
    plt.xlabel("Price")
    plt.ylabel("Quantity")
    plt.legend()
    plt.title("Demand Curve")
    plt.show()

# 3. Production Function (Cobb-Douglas)
def cobb_douglas_production_function():
    print("3. Production Function (Cobb-Douglas)")
    # Cobb-Douglas function: Q = A * L^alpha * K^beta
    A, alpha, beta = 1.2, 0.6, 0.4
    L = np.linspace(1, 100, 100)  # Labor
    K = 50  # Capital (constant for simplicity)

    Q = A * (L ** alpha) * (K ** beta)
    plt.plot(L, Q, label="Cobb-Douglas Production")
    plt.xlabel("Labor")
    plt.ylabel("Output")
    plt.title("Production Function")
    plt.legend()
    plt.show()

    print(f"Sample output for L=50, K={K}: Q = {A * (50 ** alpha) * (K ** beta):.2f}")
    print()

# 4. Game Theory (Nash Equilibrium for a 2x2 Game)
def nash_equilibrium():
    print("4. Game Theory (Nash Equilibrium)")
    # Example payoff matrices for two players
    # Player 1
    P1 = np.array([[3, 1], [0, 2]])
    # Player 2
    P2 = np.array([[2, 1], [0, 3]])

    print("Payoff matrix for Player 1:")
    print(P1)
    print("Payoff matrix for Player 2:")
    print(P2)

    # Finding Nash Equilibrium (simplistic approach)
    def best_response(player_matrix, opponent_choice):
        return np.argmax(player_matrix[:, opponent_choice])

    for i in range(2):
        for j in range(2):
            if (best_response(P1, j) == i) and (best_response(P2.T, i) == j):
                print(f"Nash Equilibrium at Player 1: Strategy {i}, Player 2: Strategy {j}")
    print()

# 5. Economic Growth Models (Solow Growth Model)
def solow_growth_model():
    print("5. Solow Growth Model")
    # Parameters
    alpha = 0.3  # Output elasticity of capital
    s = 0.2  # Savings rate
    delta = 0.1  # Depreciation rate
    n = 0.02  # Population growth rate
    A = 1  # Total factor productivity
    T = 50  # Time periods
    K = np.zeros(T)
    L = 1
    K[0] = 1  # Initial capital stock

    # Solow model capital accumulation
    for t in range(1, T):
        K[t] = s * A * (K[t - 1] ** alpha) * (L ** (1 - alpha)) + (1 - delta) * K[t - 1]

    # Plot results
    plt.plot(range(T), K, label="Capital Stock")
    plt.xlabel("Time")
    plt.ylabel("Capital")
    plt.title("Solow Growth Model")
    plt.legend()
    plt.show()

# Run examples
utility_maximization()
demand_curve_estimation()
cobb_douglas_production_function()
nash_equilibrium()
solow_growth_model()

from scipy.optimize import linprog
import networkx as nx
import numpy as np

# 1. Linear Programming
def linear_programming_example():
    print("1. Linear Programming")
    # Maximize: 3x + 2y
    # Subject to:
    # x + y <= 4
    # 2x + y <= 5
    # x, y >= 0
    c = [-3, -2]  # Coefficients for the objective function (negated for maximization)
    A = [[1, 1], [2, 1]]  # Coefficients for inequality constraints
    b = [4, 5]  # Right-hand side of the inequalities
    bounds = [(0, None), (0, None)]  # x, y >= 0
    
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    print("Optimal value:", -result.fun)
    print("Optimal solution:", result.x)
    print()

# 2. Network Optimization (Shortest Path)
def network_optimization_example():
    print("2. Network Optimization (Shortest Path)")
    G = nx.DiGraph()
    G.add_weighted_edges_from([
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'Z', 6),
        ('E', 'Z', 3)
    ])
    shortest_path = nx.shortest_path(G, source='A', target='Z', weight='weight')
    shortest_distance = nx.shortest_path_length(G, source='A', target='Z', weight='weight')
    print("Shortest path from A to Z:", shortest_path)
    print("Shortest distance:", shortest_distance)
    print()

# 3. Transportation Problem
def transportation_problem_example():
    print("3. Transportation Problem")
    # Cost matrix (rows: sources, columns: destinations)
    costs = np.array([
        [2, 3, 1],
        [5, 4, 8],
        [5, 9, 2]
    ])
    supply = [20, 30, 25]  # Supply available at each source
    demand = [30, 25, 20]  # Demand required at each destination
    
    # Solve using linear programming
    num_sources = len(supply)
    num_destinations = len(demand)
    
    c = costs.flatten()  # Flatten cost matrix to vector
    A_eq = []
    
    # Supply constraints
    for i in range(num_sources):
        row = [1 if j // num_destinations == i else 0 for j in range(num_sources * num_destinations)]
        A_eq.append(row)
    
    # Demand constraints
    for k in range(num_destinations):
        row = [1 if j % num_destinations == k else 0 for j in range(num_sources * num_destinations)]
        A_eq.append(row)
    
    b_eq = supply + demand
    bounds = [(0, None) for _ in range(num_sources * num_destinations)]
    
    result = linprog(c, A_eq=np.array(A_eq), b_eq=b_eq, bounds=bounds, method='highs')
    print("Optimal cost:", result.fun)
    print("Optimal flows:")
    print(result.x.reshape(num_sources, num_destinations))
    print()

# 4. Simulation (Queueing System)
def queue_simulation_example():
    print("4. Simulation (Queueing System)")
    import random
    random.seed(42)
    
    arrival_rate = 5  # Customers per hour
    service_rate = 6  # Customers per hour
    num_customers = 10
    
    interarrival_times = [random.expovariate(arrival_rate) for _ in range(num_customers)]
    service_times = [random.expovariate(service_rate) for _ in range(num_customers)]
    
    arrival_times = np.cumsum(interarrival_times)
    start_times = np.zeros(num_customers)
    departure_times = np.zeros(num_customers)
    
    for i in range(num_customers):
        if i == 0:
            start_times[i] = arrival_times[i]
        else:
            start_times[i] = max(arrival_times[i], departure_times[i - 1])
        departure_times[i] = start_times[i] + service_times[i]
    
    print("Arrival times:", arrival_times)
    print("Service start times:", start_times)
    print("Departure times:", departure_times)
    print("Total time in system:", departure_times - arrival_times)
    print()

# Run examples
if __name__ == "__main__":
    linear_programming_example()
    network_optimization_example()
    transportation_problem_example()
    queue_simulation_example()

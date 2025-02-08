# imports:
import random
import itertools

# functions:
def distance(p1, P_2): # calculates distance b/w two points.
    return ((p1[0] - P_2[0]) ** 2 + (p1[1] - P_2[1]) ** 2) ** 0.5

# Generate cities with random coordinates
numCities = 10
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(numCities)]

def tsp(Places):
    permutations = itertools.permutations(Places) # Get all possible orders
    minDist = float('inf')
    best_route=None # best route holder
    
    for perm in permutations:
        d = 0 # dist tracker
        for i in range(len(perm) - 1):
            d += distance(perm[i], perm[i+1]) # Add up distance.
        d += distance(perm[-1], perm[0]) # Return to start.
        if d < minDist: # check for best distance.
            minDist = d
            best_route=perm
    return best_route, minDist

# Call function to solve TSP
Optimal_Path, Shortest_Distance = tsp(cities)

print("Optimal Path:", Optimal_Path)
print("Shortest Distance:", Shortest_Distance)

#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;

// 1. Linear Programming using Simplex Method (Example)
void linearProgrammingExample() {
    cout << "1. Linear Programming" << endl;
    // Maximize: 3x + 2y
    // Subject to:
    // x + y <= 4
    // 2x + y <= 5
    // x, y >= 0

    // Coefficients of the objective function
    double c[] = {3, 2};

    // Coefficients of the constraints
    double A[2][2] = {{1, 1}, {2, 1}};
    double b[] = {4, 5};

    // Using brute force as a simple approximation
    double max_value = -numeric_limits<double>::infinity();
    pair<double, double> solution = {0, 0};

    for (double x = 0; x <= 4; x += 0.1) {
        for (double y = 0; y <= 4; y += 0.1) {
            if (x + y <= 4 && 2 * x + y <= 5) {
                double value = 3 * x + 2 * y;
                if (value > max_value) {
                    max_value = value;
                    solution = {x, y};
                }
            }
        }
    }

    cout << "Optimal value: " << max_value << endl;
    cout << "Optimal solution: x = " << solution.first << ", y = " << solution.second << endl;
    cout << endl;
}

// 2. Network Optimization (Shortest Path using Dijkstra's Algorithm)
void networkOptimizationExample() {
    cout << "2. Network Optimization (Shortest Path)" << endl;

    const int INF = numeric_limits<int>::max();
    int n = 6; // Number of nodes
    vector<vector<pair<int, int>>> graph(n);

    // Edges: (source, destination, weight)
    vector<tuple<int, int, int>> edges = {
        {0, 1, 4}, {0, 2, 2}, {1, 2, 1}, {1, 3, 5},
        {2, 3, 8}, {2, 4, 10}, {3, 4, 2}, {3, 5, 6}, {4, 5, 3}};

    for (auto &[u, v, w] : edges) {
        graph[u].emplace_back(v, w);
    }

    int source = 0, target = 5;
    vector<int> dist(n, INF), parent(n, -1);
    dist[source] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.emplace(0, source);

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u])
            continue;

        for (auto &[v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                parent[v] = u;
                pq.emplace(dist[v], v);
            }
        }
    }

    // Reconstruct shortest path
    vector<int> path;
    for (int v = target; v != -1; v = parent[v]) {
        path.push_back(v);
    }
    reverse(path.begin(), path.end());

    cout << "Shortest path: ";
    for (int node : path)
        cout << node << " ";
    cout << endl;
    cout << "Shortest distance: " << dist[target] << endl;
    cout << endl;
}

// 3. Simulation (Queueing System)
void queueSimulationExample() {
    cout << "3. Simulation (Queueing System)" << endl;

    srand(static_cast<unsigned>(time(0)));

    int num_customers = 10;
    double arrival_rate = 5;  // Customers per hour
    double service_rate = 6; // Customers per hour

    vector<double> interarrival_times(num_customers);
    vector<double> service_times(num_customers);
    vector<double> arrival_times(num_customers);
    vector<double> start_times(num_customers);
    vector<double> departure_times(num_customers);

    for (int i = 0; i < num_customers; ++i) {
        interarrival_times[i] = -log((double)rand() / RAND_MAX) / arrival_rate;
        service_times[i] = -log((double)rand() / RAND_MAX) / service_rate;
    }

    arrival_times[0] = interarrival_times[0];
    start_times[0] = arrival_times[0];
    departure_times[0] = start_times[0] + service_times[0];

    for (int i = 1; i < num_customers; ++i) {
        arrival_times[i] = arrival_times[i - 1] + interarrival_times[i];
        start_times[i] = max(arrival_times[i], departure_times[i - 1]);
        departure_times[i] = start_times[i] + service_times[i];
    }

    cout << "Customer | Arrival Time | Start Time | Departure Time | Total Time in System" << endl;
    for (int i = 0; i < num_customers; ++i) {
        cout << setw(8) << i + 1 << " | " << setw(12) << fixed << setprecision(2) << arrival_times[i]
             << " | " << setw(10) << start_times[i] << " | " << setw(14) << departure_times[i]
             << " | " << setw(20) << departure_times[i] - arrival_times[i] << endl;
    }
    cout << endl;
}

// Main function to run examples
int main() {
    linearProgrammingExample();
    networkOptimizationExample();
    queueSimulationExample();
    return 0;
}

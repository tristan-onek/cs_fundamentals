#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <list>
#include <algorithm>
using namespace std;

int main() {
    cout << "Data Structures Fundamentals in C++\n" << endl;

    // 1. Array
    cout << "1. Array\n";
    int arr[] = {1, 2, 3, 4, 5}; // Static array
    cout << "Array elements: ";
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";

    // 2. Vector (Dynamic Array)
    cout << "\n2. Vector (Dynamic Array)\n";
    vector<int> vec = {10, 20, 30};
    vec.push_back(40); // Adding an element
    vec.push_back(50);
    cout << "Vector elements: ";
    for (int val : vec) cout << val << " ";
    cout << "\n";

    // 3. Stack (LIFO)
    cout << "\n3. Stack (LIFO)\n";
    stack<int> stk;
    stk.push(1);
    stk.push(2);
    stk.push(3);
    cout << "Top of stack: " << stk.top() << endl; // Top element
    stk.pop(); // Remove top element
    cout << "Top after pop: " << stk.top() << endl;

    // 4. Queue (FIFO)
    cout << "\n4. Queue (FIFO)\n";
    queue<int> q;
    q.push(5);
    q.push(10);
    q.push(15);
    cout << "Front of queue: " << q.front() << endl;
    q.pop(); // Remove front element
    cout << "Front after pop: " << q.front() << endl;

    // 5. Priority Queue (Heap)
    cout << "\n5. Priority Queue (Heap)\n";
    priority_queue<int> pq; // Max-heap by default
    pq.push(20);
    pq.push(5);
    pq.push(15);
    cout << "Top of max-heap: " << pq.top() << endl;
    pq.pop(); // Remove top
    cout << "Top after pop: " << pq.top() << endl;

    // Min-heap using priority_queue
    priority_queue<int, vector<int>, greater<int>> minHeap;
    minHeap.push(20);
    minHeap.push(5);
    minHeap.push(15);
    cout << "Top of min-heap: " << minHeap.top() << endl;

    // 6. Set (Ordered Collection)
    cout << "\n6. Set (Ordered Collection)\n";
    set<int> s = {10, 20, 10, 30}; // Duplicates are removed
    cout << "Set elements: ";
    for (int val : s) cout << val << " ";
    cout << "\n";

    // 7. Unordered Set (Hash Table)
    cout << "\n7. Unordered Set (Hash Table)\n";
    unordered_set<int> us = {10, 20, 10, 30};
    cout << "Unordered Set elements: ";
    for (int val : us) cout << val << " ";
    cout << "\n";

    // 8. Map (Key-Value Pairs)
    cout << "\n8. Map (Key-Value Pairs)\n";
    map<string, int> mp;
    mp["apple"] = 5;
    mp["banana"] = 3;
    mp["cherry"] = 7;
    cout << "Map elements:\n";
    for (auto [key, value] : mp) {
        cout << key << ": " << value << endl;
    }

    // 9. Unordered Map (Hash Table for Key-Value Pairs)
    cout << "\n9. Unordered Map (Hash Table)\n";
    unordered_map<string, int> ump;
    ump["car"] = 10;
    ump["bike"] = 20;
    ump["bus"] = 30;
    cout << "Unordered Map elements:\n";
    for (auto [key, value] : ump) {
        cout << key << ": " << value << endl;
    }

    // 10. Linked List
    cout << "\n10. Linked List\n";
    list<int> linkedList = {1, 2, 3, 4, 5};
    linkedList.push_front(0); // Add to front
    linkedList.push_back(6); // Add to back
    cout << "Linked List elements: ";
    for (int val : linkedList) cout << val << " ";
    cout << "\n";

    // 11. Deque (Double-Ended Queue)
    cout << "\n11. Deque (Double-Ended Queue)\n";
    deque<int> dq = {1, 2, 3};
    dq.push_front(0); // Add to front
    dq.push_back(4); // Add to back
    cout << "Deque elements: ";
    for (int val : dq) cout << val << " ";
    cout << "\n";

    // 12. Binary Search (Algorithm)
    cout << "\n12. Binary Search\n";
    vector<int> searchVec = {1, 3, 5, 7, 9};
    int key = 5;
    bool found = binary_search(searchVec.begin(), searchVec.end(), key);
    cout << "Is " << key << " in the vector? " << (found ? "Yes" : "No") << endl;

    // 13. Sorting (Algorithm)
    cout << "\n13. Sorting\n";
    vector<int> sortVec = {5, 3, 8, 1, 2};
    sort(sortVec.begin(), sortVec.end());
    cout << "Sorted vector: ";
    for (int val : sortVec) cout << val << " ";
    cout << "\n";

    return 0;
}

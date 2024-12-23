//imports:
import java.util.*;
//end imports

//begin main class content:
public class BasicDataStructures {

    public static void main(String[] args) 
    {
        // 1. Arrays:
        System.out.println("#1. Arrays");
        int[] array = {10, 20, 30, 40, 50};
        System.out.println("Array element at index 2: " + array[2]);

        // 2. Array Lists:
        System.out.println("\n#2. ArrayList");
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(10);
        arrayList.add(20);
        arrayList.add(30);
        arrayList.remove(1);
        System.out.println("ArrayList after adding and removing elements: " + arrayList);

        // 3. Linked Lists:
        System.out.println("\n#3. LinkedList");
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.add("A");
        linkedList.add("B");
        linkedList.add("C");
        linkedList.removeFirst();
        System.out.println("LinkedList after modifications: " + linkedList);

        // 4. Stacking:
        System.out.println("\n4. Stack");
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("Top of stack: " + stack.peek());
        stack.pop();
        System.out.println("Stack after pop: " + stack);

        // 5. Queueing:
        System.out.println("\n5. Queue");
        Queue<String> queue = new LinkedList<>();
        queue.add("Alice");
        queue.add("Bob");
        queue.add("Charlie");
        System.out.println("Front of queue: " + queue.peek());
        queue.remove();
        System.out.println("Queue after removing the front: " + queue);

        // 6. Priority Queues:
        System.out.println("\n6. Priority Queue");
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(5);
        minHeap.add(1);
        minHeap.add(3);
        System.out.println("Priority Queue (Min-Heap) head: " + minHeap.peek());
        minHeap.poll();
        System.out.println("Priority Queue after polling: " + minHeap);

        // 7. HashMap:
        System.out.println("\n7. HashMap");
        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("One", 1);
        hashMap.put("Two", 2);
        hashMap.put("Three", 3);
        System.out.println("Value for key 'Two': " + hashMap.get("Two"));

        // 8. HashSet:
        System.out.println("\n8. HashSet");
        HashSet<String> hashSet = new HashSet<>();
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Cherry");
        hashSet.add("Apple"); // Duplicate, won't be added
        System.out.println("HashSet content: " + hashSet);

        // 9. TreeMap:
        System.out.println("\n9. TreeMap");
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("Cat", 3);
        treeMap.put("Dog", 5);
        treeMap.put("Elephant", 10);
        System.out.println("TreeMap content (sorted by key): " + treeMap);

        // 10. TreeSet:
        System.out.println("\n10. TreeSet");
        TreeSet<Integer> treeSet = new TreeSet<>();
        treeSet.add(10);
        treeSet.add(5);
        treeSet.add(20);
        System.out.println("TreeSet (sorted): " + treeSet);

        // 11. Graph:
        System.out.println("\n11. Graph (Adjacency List)");
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(1, Arrays.asList(2, 3));
        graph.put(2, Arrays.asList(4));
        graph.put(3, Arrays.asList(4));
        graph.put(4, new ArrayList<>());
        System.out.println("Graph adjacency list: " + graph);

        // 12. Binary Tree:
        System.out.println("\n12. B Trees");
        BinaryTree tree = new BinaryTree();
        tree.root = new TreeNode(1);
        tree.root.left = new TreeNode(2);
        tree.root.right = new TreeNode(3);
        tree.root.left.left = new TreeNode(4);
        System.out.print("Binary Tree In-Order Traversal: ");
        tree.inOrderTraversal(tree.root);
        System.out.println();
    }
}

// Binary Tree Structure
class tNode 
{
    int data;
    tNode left, right;

    tNode(int data) 
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class bTree {
    tNode root;

    void inOrderTraversal(tNode node) {
        if (node == null) return;
        inOrderTraversal(node.left);
        System.out.print(node.data + " ");
        inOrderTraversal(node.right);
    }
}

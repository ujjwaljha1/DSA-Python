# Data Structures and Algorithms in Python

Welcome to the Data Structures and Algorithms (DSA) repository. This repository covers DSA concepts from beginner to advanced levels, with Python implementations and explanations for each topic.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Python Basics](#python-basics)
   - [if-else Statements](#if-else-statements)
   - [for Loops](#for-loops)
   - [while Loops](#while-loops)
   - [break Statement](#break-statement)
   - [continue Statement](#continue-statement)
4. [Data Structures](#data-structures)
   - [Arrays](#arrays)
   - [Linked Lists](#linked-lists)
   - [Stacks](#stacks)
   - [Queues](#queues)
   - [Hash Tables](#hash-tables)
   - [Trees](#trees)
   - [Graphs](#graphs)
   - [Heaps](#heaps)
   - [Tries](#tries)
5. [Algorithms](#algorithms)
   - [Sorting Algorithms](#sorting-algorithms)
   - [Searching Algorithms](#searching-algorithms)
   - [Dynamic Programming](#dynamic-programming)
   - [Greedy Algorithms](#greedy-algorithms)
   - [Backtracking](#backtracking)
   - [Graph Algorithms](#graph-algorithms)
   - [String Algorithms](#string-algorithms)
6. [Contributing](#contributing)


## Introduction

This repository aims to provide a comprehensive guide to Data Structures and Algorithms (DSA) using Python. It includes explanations, example code, and practical applications for each topic, making it suitable for beginners and advanced learners alike.

## Getting Started

To get started, clone this repository to your local machine using:

```bash
git clone https://github.com/ujjwaljha1/dsa-python.git
cd dsa-python
```

Ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

## Python Basics

### if-else Statements

The `if` statement is used for conditional execution. The `else` clause can be used to execute a block of code if the condition is false.

```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

### for Loops

The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).

```python
for i in range(5):
    print(i)
```

### while Loops

The `while` loop is used to execute a block of code as long as a condition is true.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### break Statement

The `break` statement is used to exit the loop prematurely.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### continue Statement

The `continue` statement is used to skip the rest of the code inside the loop for the current iteration only.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

## Data Structures

### Arrays

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.

### Linked Lists

A linked list is a linear data structure where each element is a separate object, called a node. Each node contains data and a reference to the next node in the sequence.

### Stacks

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. It allows insertion and deletion of elements only at one end, called the top.

### Queues

A queue is a linear data structure that follows the FIFO (First In First Out) principle. Elements are added at the rear and removed from the front.

### Hash Tables

A hash table is a data structure that implements an associative array, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots.

### Trees

A tree is a hierarchical data structure consisting of nodes, with a designated node called the root, from which all other nodes branch out.

### Graphs

A graph is a collection of nodes (vertices) and edges connecting them. Graphs can be directed or undirected, weighted or unweighted.

### Heaps

A heap is a special tree-based data structure that satisfies the heap property. In a max heap, for any given node, the value of the node is greater than or equal to the values of its children, and the highest value is at the root.

### Tries

A trie is a special type of tree used to store associative data structures. A common application of a trie is storing a predictive text or autocomplete dictionary.

## Algorithms

### Sorting Algorithms

Sorting algorithms are used to rearrange elements in a list or array in a certain order (ascending or descending).

- [Bubble Sort](#)
- [Insertion Sort](#)
- [Selection Sort](#)
- [Merge Sort](#)
- [Quick Sort](#)
- [Heap Sort](#)

### Searching Algorithms

Searching algorithms are designed to retrieve an element from any data structure where it is stored.

- [Linear Search](#)
- [Binary Search](#)

### Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and solving each of them just once, storing their solutions.

### Greedy Algorithms

Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit.

### Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to computational problems, notably constraint satisfaction problems.

### Graph Algorithms

Graph algorithms are a set of instructions that traverse (visits nodes of) a graph.

- [Depth-First Search (DFS)](#)
- [Breadth-First Search (BFS)](#)
- [Dijkstra's Algorithm](#)
- [Bellman-Ford Algorithm](#)

### String Algorithms

String algorithms deal with problems involving string manipulation and searching within strings.

- [Knuth-Morris-Pratt (KMP) Algorithm](#)
- [Rabin-Karp Algorithm](#)

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before making a contribution.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Problems and Implementations

### List

- [Accessing the List](List/Accessing%20the%20list.py)
- [Average or Mean of a List](List/Average%20or%20Mean%20of%20a%20List.py)
- [Check if a List is Sorted (Effective)](List/Check%20if%20a%20list%20is%20Sorted%20Effective.py)
- [Check if a List is Sorted (Naive)](List/Check%20if%20a%20list%20is%20Sorted%20Naive.py)
- [Insert and Search](List/Insert%20and%20search.py)
- [Left Rotate a List by One (Effective)](List/Left%20Rotate%20a%20List%20by%20one%20Effective.py)
- [Left Rotate a List by One (Slice, Append POP)](List/Left%20Rotate%20a%20List%20by%20one%20Slice,%20append%20POP.py)
- [List Slicing](List/List%20slicing.py)
- [Removal of Items](List/Removal%20of%20items.py)
- [Separate Even and Odd](List/Separate%20Even%20and%20Odd.py)
- [Some General-Purpose List Operations](List/Some%20general-purpose.py)
- [Working with Lists, Tuples, and Strings](List/w%20list,%20tuple%20and%20string.py)

### List - LeetCode Problems

- [Left Rotate by d Places (Direct Method)](List/LeetCode%20Problems/Left%20Rotate%20by%20d%20Places%20Direct%20Method.py)
- [Maximum Difference Between Increasing Elements (LeetCode)](List/LeetCode%20Problems/Maximum%20Difference%20Between%20Increasing%20Elements%20LeetCode.py)
- [Maximum Difference (Efficient)](List/LeetCode%20Problems/Maximum%20difference%20Efficient.py)
- [Maximum Difference (Naive)](List/LeetCode%20Problems/Maximum%20difference%20Naive.py)
- [Right Rotate (LeetCode)](List/LeetCode%20Problems/Right%20Rotate%20LeetCode.py)

### Mathematics

- [Check for Prime (Efficient)](Mathematics/Check%20for%20Prime%20Efficient.py)
- [Check for Prime (Naive)](Mathematics/Check%20for%20Prime%20Naive.py)
- [Count Numbers](Mathematics/CountNumbers.py)
- [Factorial](Mathematics/Factorial.py)
- [GCD](Mathematics/GCD.py)
- [GCD2](Mathematics/GCD2.py)
-

 [LCM of Two Numbers (Efficient)](Mathematics/LCM%20of%20two%20Numbers%20Efficient.py)
- [LCM of Two Numbers (Naive)](Mathematics/LCM%20Of%20two%20Numbers%20Naive.py)
- [Palindrome](Mathematics/Palindrome.py)
- [Prime Factorization](Mathematics/Prime%20Factorization.py)
- [Sieve of Eratosthenes](Mathematics/Sieve%20of%20Eratosthenes.py)
- [Square Root (Effective)](Mathematics/Square%20Root%20Effective.py)
- [Square Root (Naive)](Mathematics/Square%20Root%20Naive.py)
- [Sum of Natural Numbers](Mathematics/SumofNaturalNumbers.py)

### Recursion

- [Rope Cutting Problem](Recursion/Rope%20Cutting%20Problem.py)

### Searching

- [Binary Search](Searching/Binary%20Search%20in%20Python.py)
- [Count 1's in a Sorted Binary List (Binary)](Searching/Count%201's%20in%20a%20Sorted%20Binary%20List%20Binary.py)
- [Count 1's in a Sorted Binary List (Recursive)](Searching/Count%201's%20in%20a%20Sorted%20Binary%20List%20Recurssive.py)
- [Count Occurrences in a Sorted Array (Effective)](Searching/Count%20Occurrences%20in%20a%20Sorted%20Array%20Effective.py)
- [Count Occurrences in a Sorted Array](Searching/Count%20Occurrences%20in%20a%20Sorted%20Array.py)
- [Index of First Occurrence in a Sorted Array (Efficient)](Searching/Index%20of%20First%20Occurrence%20in%20a%20Sorted%20Array%20Efficient.py)
- [Index of First Occurrence in a Sorted Array (Naive)](Searching/Index%20of%20First%20Occurrence%20in%20a%20Sorted%20Array%20Naive.py)
- [Index of Last Occurrence (Effective)](Searching/Index%20of%20Last%20Occurrence%20Effective.py)
- [Index of Last Occurrence](Searching/Index%20of%20Last%20Occurrence.py)
- [Recursive Binary Search](Searching/Recursive%20Binary%20Search%20in%20Python.py)

---

Feel free to explore the topics and implementations. If you find any issues or have suggestions, please contribute to the project.

# MSCS532_Assignment6
## Description
This project implements several core data structures from scratch in Python, along with two selection algorithms for finding the k-th smallest element. The goal was to understand internal behavior, performance characteristics, and real-world applications.

Implemented components:

Deterministic and Randomized Selection Algorithms
Arrays and Matrices
Stacks and Queues (using arrays)
Singly Linked Lists
Rooted Trees (optional)

## How to Run the Code
Requirements
Python 3.6 or higher

Setup Instructions
Clone the repository:
git clone https://github.com/snevoji35690/MSCS532_Assignment6.git
cd MSCS532_Assignment6

MSCS532_Assignment6/
│
├── Elementary data structures.py       # All data structure implementations and test output
├── README.md               
├── Selection algorithms.py 

## Selection Algorithm Explanations
Deterministic Selection (Median of Medians)
Guarantees worst-case linear time.
Divides the array into groups of 5, finds medians, and recursively selects the median of those medians as the pivot.
Ensures that a good portion of the array is discarded each step, avoiding worst-case behavior.
Ideal when predictable performance is required, regardless of input.

## Randomized Quickselect
Fast and simple in practice, with expected time complexity of O(n).
Randomly selects a pivot and recursively selects within the correct partition.
Works well on average but can degrade to O(n²) in rare worst-case scenarios.
Suitable for general use unless the input is adversarial.

## Time Complexity Analysis
Structure/Algorithm	Operation	Time Complexity	Why?
Array	Insert / Delete (middle)	O(n)	Shifting needed
Access (by index)	O(1)	Direct access
Matrix	Access / Modify	O(1)	Indexed grid
Stack (Array)	Push / Pop	O(1)	End of list
Queue (Array)	Enqueue	O(1)	Append at end
Dequeue	O(n)	Shift left
Linked List	Insert / Delete (head)	O(1)	No shift needed
Traverse / Search	O(n)	Must walk through
Tree	Add Child / Traverse	O(1) / O(n)	Depends on depth
Randomized Select	Expected Case	O(n)	Good average splits
Worst Case	O(n²)	Poor random pivoting
Deterministic Select	Worst Case	O(n)	Uses median-of-medians to guarantee balance


## Summary of Findings
Arrays are best for fast lookups but inefficient for frequent modifications.
Stacks and queues are ideal for LIFO/FIFO behaviors and sequential workflows.
Linked lists provide dynamic memory management for insert-heavy tasks.
Trees model hierarchical structures and support recursive operations well.
Deterministic selection ensures stable performance, while randomized quickselect is faster on average.

## Conclusion
This assignment offered valuable hands-on experience in building fundamental data structures and understanding their algorithmic trade-offs. By implementing and analyzing each structure manually, we gained deeper insights into time complexity, space usage, and real-world suitability — skills essential for writing efficient and scalable code.


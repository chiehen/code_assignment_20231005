# Priority queue with possibility to change key value
## Task Description
Some algorithms (like Dijkstra shortest path algorithm) require a priority queue that supports modification of the key (priority value).
It is required to implement such container based on heap data structure.

The solution should be tested.

## Installation
1. Have python3, pip installed
2. Install dependency
`pip install -r requirements.txt`

## Interface
```python
from PriorityQueue import PriorityQueue

queue = PriorityQueue()

# insert value and specify priority (the lowest number has the top priority)
queue.insert(val="two", priority=2)

# change the priority value of specific value
queue.change_priority(val="two", priority=1)

# return value at the front (with the top priority)
queue.peek() # return "two"

# return value at the front (with the top priority), and remove the elelment

queue.dequeue() # return "two"

```

## Test
run `pytest`

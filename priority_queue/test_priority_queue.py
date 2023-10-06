from PriorityQueue import PriorityQueue as Queue
from Element import Element


def test_insert():
    queue = Queue()

    assert queue.peek() is None

    queue.insert("two", 2)

    assert queue.peek() == "two"

    queue.insert("one", 1)
    queue.insert("three", 3)

    assert queue.peek() == "one"


def test_dequeue():
    queue = Queue()

    queue.insert("two", 2)
    queue.insert("one", 1)
    queue.insert("four", 4)
    queue.insert("three", 3)
    queue.insert("five", 5)

    assert queue.dequeue() == "one"
    assert queue.dequeue() == "two"
    assert queue.dequeue() == "three"
    assert queue.dequeue() == "four"
    assert queue.dequeue() == "five"
    assert queue.dequeue() is None


def test_change_priority():
    queue = Queue()

    queue.insert("two", 2)
    queue.insert("seven_then_one", 7)
    queue.insert("four", 4)
    queue.insert("three_then_six", 3)
    queue.insert("five", 5)

    queue.change_priority("seven_then_one", 1)
    queue.change_priority("three_then_six", 6)

    assert queue.dequeue() == "seven_then_one"
    assert queue.dequeue() == "two"
    assert queue.dequeue() == "four"
    assert queue.dequeue() == "five"
    assert queue.dequeue() == "three_then_six"

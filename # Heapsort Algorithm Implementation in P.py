# Heapsort Algorithm Implementation in Python

def max_heapify(arr, n, i):
    """
    Maintains the Max-Heap property for a given node.
    :param arr: List of numbers
    :param n: Size of the heap
    :param i: Index of the node
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Builds a Max-Heap from an unordered list.
    :param arr: List of numbers
    """
    n = len(arr)
    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    """
    Sorts an array using the HeapSort algorithm.
    :param arr: List of numbers
    """
    n = len(arr)
    build_max_heap(arr)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        max_heapify(arr, i, 0)  # Heapify the root

if name == "__main__":
    # Example usage
    arr = [4, 10, 3, 5, 1]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)
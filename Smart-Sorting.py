import heapq

def _preview(values, limit=8):
    return f"{values[:limit]}{'...' if len(values) > limit else ''}"

def parse_input_numbers(raw):
    tokens = raw.replace(",", " ").split()
    return [float(token) if "." in token else int(token) for token in tokens]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def heap_sort(arr):
    heap = arr.copy()
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x <  pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x >  pivot]
    return quick_sort(left) + middle + quick_sort(right)

def sorting_in_python(arr):
    return sorted(arr)

def analyse(arr):
    """Return key traits of the input list."""
    n = len(arr)
    if n == 0:
        return {
            "size": 0,
            "nearly_sorted": True,
            "duplicates": False,
        }

    pairs = n - 1
    sorted_pairs = sum(1 for i in range(pairs) if arr[i] <= arr[i+1])
    return {
        "size":          n,
        "nearly_sorted": pairs > 0 and sorted_pairs / pairs > 0.90,
        "duplicates":    len(set(arr)) / n < 0.20,
    }

def smart_sort(arr):
    """Analyse arr and sort with the best-fit algorithm."""
    data = arr.copy()
    info = analyse(data)
    n    = info["size"]

    if n <= 10:
        algo = "Bubble Sort"
        result = bubble_sort(data)
    elif n <= 20:
        algo = "Selection Sort"
        result = selection_sort(data)
    elif info["nearly_sorted"]:
        algo = "Insertion Sort  (nearly sorted → O(n) best case)"
        result = insertion_sort(data)
    elif info["duplicates"]:
        algo = "Heap Sort  (many duplicates → stable O(n log n))"
        result = heap_sort(data)
    elif n <= 5000:
        algo = "Quick Sort  (medium, random data → fastest in practice)"
        result = quick_sort(data)
    else:
        algo = "Sorting in Python  (highly optimized general-purpose sort)"
        result = sorting_in_python(data)

    print(f"Input  : {_preview(arr)}")
    print(f"Size   : {n}")
    print(f"Chosen : {algo}")
    print(f"Output : {_preview(result)}\n")
    return result

if __name__ == "__main__":
    raw = input("Enter numbers to sort (comma or space separated): ").strip()

    if not raw:
        print("No input provided.")
    else:
        try:
            data = parse_input_numbers(raw)
            smart_sort(data)
        except ValueError:
            print("Invalid input. Please enter only numbers separated by commas or spaces.")
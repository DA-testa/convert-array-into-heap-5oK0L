def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def sift_down(arr, i, swaps):
    n = len(arr)
    min_index = i
    l = left_child(i)
    if l < n and arr[l] < arr[min_index]:
        min_index = l
    r = right_child(i)
    if r < n and arr[r] < arr[min_index]:
        min_index = r
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, swaps)

def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(arr, i, swaps)
    return swaps

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    swaps = build_heap(arr)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

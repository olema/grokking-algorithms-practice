arr = [1,3,5,0,10,20,11,15,25]
item = arr[5]

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

print(binary_search(arr, 3))
print(binary_search(arr,26))

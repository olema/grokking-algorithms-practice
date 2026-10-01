def sum_rec(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_rec([i for i in arr[1:]])

arr = [12,12,13]
print(f"sum of {arr} = {sum_rec(arr)}")

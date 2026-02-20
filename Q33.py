def maxDif(arr):
    min_ele = arr[0]
    max_diff = arr[1] - arr[0]

    for j in range(1, len(arr)):
        max_diff = max(max_diff, arr[j] - min_ele)
        min_ele = min(min_ele, arr[j])

    return max_diff

arr = [2, 3, 10, 6, 4, 8, 1]
print(maxDif(arr))
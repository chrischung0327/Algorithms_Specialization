def partition(arr, low, high):
    
    pivot = arr[low]

    i, j = low+1, low+1
    while j <= high:
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
            
    arr[i-1], arr[low] = arr[low], arr[i-1]
    return i-1, high-low


def quickSort(arr: list, low, high):
    '''
    Implement in-place solution
    '''
    cnt = 0
    if low < high:
        pivot, _cnt = partition(arr, low, high)
        _cnt_left = quickSort(arr, low, pivot-1)
        _cnt_right = quickSort(arr, pivot+1, high)
        cnt += _cnt + _cnt_left + _cnt_right
    
    return cnt



test_cases = [[8,3,4,5,9,2,4,6], [1,2,3,5,6,9], [2,1], [9,6,5,2,1]]
for t in test_cases:
    _cnt = quickSort(t, 0, len(t)-1)
    print(t, _cnt)

f = open("test_case.txt", "r")
lines = [int(x.strip()) for x in f.readlines()]
f.close()

cnt = quickSort(lines, 0, len(lines)-1)
print("Answer is: ", cnt)
# 162085
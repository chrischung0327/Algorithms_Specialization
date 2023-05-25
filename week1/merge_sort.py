def mergeSort(arr: list) -> list:
    if arr == [] or len(arr)==1:
        return arr
    if len(arr)>2:
        mid = len(arr) // 2
        arr = _merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
    else:
        arr[0], arr[1] = min(arr), max(arr)
    return arr


def _merge(arr1: list, arr2: list) -> list:
    i, a, b = 0, 0, 0
    ret = [0] * (len(arr1)+len(arr2))
    while a < len(arr1) or b < len(arr2):
        if a == len(arr1):
            ret[i] = arr2[b]
            b += 1
            i += 1
            continue
        if b == len(arr2):
            ret[i] = arr1[a]
            a += 1
            i += 1
            continue
        if arr1[a] < arr2[b]:
            ret[i] = arr1[a]
            a += 1
            i += 1
        else:
            ret[i] = arr2[b]
            b += 1
            i += 1

    return ret



test_cases = [[1,3,4,5,9,2,4,6], [1,2,3,5,6,9], [2,1], [9,6,5,2,1]]
for t in test_cases:
    print(mergeSort(t))
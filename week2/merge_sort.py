def mergeSort_and_count(arr: list):
    cnt = 0
    if arr == [] or len(arr)==1:
        return arr, cnt
    if len(arr)>2:
        mid = len(arr) // 2
        left_arr, left_cnt = mergeSort_and_count(arr[:mid])
        right_arr, right_cnt = mergeSort_and_count(arr[mid:])
        arr, merge_cnt = _merge_and_count(left_arr, right_arr)
        cnt += left_cnt + right_cnt + merge_cnt
    else:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            cnt += 1
    return arr, cnt


def _merge_and_count(arr1: list, arr2: list):
    i, a, b = 0, 0, 0
    cnt = 0
    ret = [0] * (len(arr1)+len(arr2))
    while a < len(arr1) or b < len(arr2):
        if a == len(arr1):
            ret[i] = arr2[b]
            b += 1
            i += 1
            if i > b+len(arr1):
                cnt += i-(b+len(arr1))
            continue
        if b == len(arr2):
            ret[i] = arr1[a]
            a += 1
            i += 1
            if i > a:
                cnt += i-a
            continue
        if arr1[a] < arr2[b]:
            ret[i] = arr1[a]
            a += 1
            i += 1
            if i > a:
                cnt += i-a
        else:
            ret[i] = arr2[b]
            b += 1
            i += 1
            if i > b+len(arr1):
                cnt += i-(b+len(arr1))

    return ret, cnt



test_cases = [[1,3,4,5,9,2,4,6], [1,2,3,5,6,9], [2,1], [9,6,5,2,1]]
for t in test_cases:
    print(mergeSort_and_count(t))

f = open("test_case.txt", "r")
lines = [int(x.strip()) for x in f.readlines()]
f.close()

_, cnt = mergeSort_and_count(lines)
print("Answer is: ", cnt)
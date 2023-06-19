def load_data(name: str):
    f = open(name, "r")
    lines = [int(x.strip()) for x in f.readlines()][1:]
    f.close()
    return lines


def _get_length_of_huffman_coding(arr):
    data = {i: k for i,k in enumerate(arr)}
    levels = [[i] for i in range(len(data))]
    cnt = len(data)
    while len(data) > 2:
        # first item
        _min1 = min(data, key=data.get)
        min1  = data.pop(_min1)
        # second item
        _min2 = min(data, key=data.get)
        min2  = data.pop(_min2)
        # Add combination back
        data[cnt] = min1+min2
        levels += [levels[_min1] + levels[_min2]]
        cnt += 1

    bytes = [0] * len(arr)

    for level in levels:
        for item in level:
            bytes[item] += 1
    
    return bytes
    


def main():
    arr = load_data('huffman.txt')
    bytes = _get_length_of_huffman_coding(arr)
    print("Maximum Length is: ", max(bytes))
    print("Minimum Length is: ", min(bytes))


if __name__ == '__main__':
    main()
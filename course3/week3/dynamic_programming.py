def load_data(name: str):
    f = open(name, "r")
    lines = [int(x.strip()) for x in f.readlines()][1:]
    f.close()
    return lines



def dynamic_programming(arr):
    n = len(arr)
    mwis = [0] * (n+1)
    solution = [[] for _ in range(n+1)]

    # Init
    mwis[1] = arr[1]
    solution[1] = [1]

    for i in range(2, n+1):
        mwis[i] = max(mwis[i-2]+arr[i-1], mwis[i-1]) # compare (cumulated sum to i-2 add item i-1) vs (cumulated sum to i-1)
        if mwis[i-2]+arr[i-1] > mwis[i-1]:
            solution[i] = solution[i-2]+[i]
        else:
            solution[i] = solution[i-1].copy()

    return solution[-1]

def main():
    arr = load_data('mwis.txt')
    target = [1, 2, 3, 4, 17, 117, 517, 997]
    solution = dynamic_programming(arr)
    print('Answer is: ', ''.join(['1' if i in solution else '0' for i in target]))


if __name__ == '__main__':
    main()
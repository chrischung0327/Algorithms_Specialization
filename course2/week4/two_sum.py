from numba import njit


def load_data(name: str):
    f = open(name, "r")
    lines = set([int(x.strip()) for x in f.readlines()])
    f.close()
    return lines


# njit for set is deprecated but still faster
@njit()
def two_sum(raw):
    cnt = 0
    for target in range(-10000,10001):
        for number in raw:
            # ensuring distinctness
            if target-number in raw and target-number != number:
                cnt += 1
                print('Found:', cnt)
                break
    return cnt
        


def main():
    '''
    Set in python is also using hash for container type
    '''
    # Load data
    cnt = 0
    raw = load_data("test_data.txt")
    cnt = two_sum(raw)

    return cnt


if __name__ == '__main__':
    cnt = main()
    print('Final count:', cnt)
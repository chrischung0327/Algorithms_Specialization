import numpy as np
from tqdm.auto import tqdm


def load_data(name: str):
    f = open(name, "r")
    lines = [[int(y) for y in x.split()] for x in f.readlines()]
    knapsack_size, number_of_item = lines[0]
    f.close()
    return lines[1:], knapsack_size, number_of_item 


def knapsack_solver(data, knapsack_size, number_of_item):
    '''
    Max: vj*xj
    s.t. wj*xj <= W
    '''
    v, w = [x[0] for x in data], [x[1] for x in data]
    # matrix = [[0]*knapsack_size for _ in range(number_of_item+1)] 
    current = [0] * knapsack_size
    next_item = [0] * knapsack_size
    for i in tqdm(range(1, number_of_item+1)):
        for j in range(knapsack_size):
            # we put item i in bag, when bag is still available: 
            # if j >= w[i-1] -> max_value(without_item-i, with_item-i)
            next_item[j] = max(current[j], current[j-w[i-1]]+v[i-1]) if j >= w[i-1] else current[j]
        current = next_item.copy()
    return next_item[-1]


def knapsack_solver_efficient(data, knapsack_size, number_of_item):
    '''
    Using array operation
    '''
    v, w = np.array([x[0] for x in data]), np.array([x[1] for x in data])
    current = np.zeros(knapsack_size)
    for i in tqdm(range(1, number_of_item+1)):
        replace   = shift(current, w[i-1]) + v[i-1]
        size      = np.concatenate((np.zeros(w[i-1]), np.ones(knapsack_size-w[i-1])))
        next_item = np.array([current, replace]).max(axis=0) * size + current * (1-size)
        current   = next_item
    return current[-1]


def shift(arr, num, fill_value=0):
    if num >= 0:
        return np.concatenate((np.full(num, fill_value), arr[:-num]))
    else:
        return np.concatenate((arr[-num:], np.full(-num, fill_value)))


def main():
    data, knapsack_size, number_of_item = load_data('knapsack_big.txt')
    answer = knapsack_solver_efficient(data, knapsack_size, number_of_item )
    print("Answer is: ", answer)


if __name__ == '__main__':
    main()
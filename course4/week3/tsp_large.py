import numpy as np
from tqdm.auto import tqdm


def load_data(name):
    file = open(name,'r')
    data = file.readlines()
    
    n = int(data[0].split()[0])
    A = np.zeros((n, 2))

    for i, line in enumerate(data[1:]):
        A[i, :] = np.array([float(x) for x in line.split()][1:])
    return A


def tsp(A):
    N = len(A)
    travel = 0
    visited = np.zeros(N)
    visited[0] = 1
    init = A[0]
    for _ in tqdm(range(N-1)):
        distance_matrix = ((init[0] - A[:, 0])**2 + (init[1] - A[:, 1])**2) * (1-visited)
        d = min(distance_matrix[distance_matrix != 0])
        city = np.where(distance_matrix==d)[0][0]
        travel += np.sqrt(d)
        init = A[city]
        visited[city] = 1

    # Go back home
    travel += np.sqrt(((A[0][0] - A[city][0])**2 + (A[0][1] - A[city][1])**2))
    return travel


def main():
    A = load_data('nn.txt')
    tsp_ = tsp(A)
    print("Answer is: ", int(tsp_))


if __name__ == '__main__':
    main()
import numpy as np
from tqdm.auto import tqdm
from itertools import combinations


def build_distance_matrix(A):
    '''
    Build the distance matrix
    '''
    mat = np.sqrt((A[:, 0, np.newaxis] - A[:, 0])**2 + (A[:, 1, np.newaxis] - A[:, 1])**2)
    mat[mat == 0] = np.inf
    return mat
    

def load_data(name):
    file = open(name,'r')
    data = file.readlines()
    
    n = int(data[0].split()[0])
    A = np.zeros((n, 2))

    for i, line in enumerate(data[1:]):
        A[i, :] = np.array([float(x) for x in line.split()])
    return A


def tsp(distance_matrix):
    N = len(distance_matrix)
    previous = {(0): {0: 0}}

    for i in range(1, N):
        current = {(tuple(c)): {tuple(c)[j]: 0 for j in range(i)} for c in combinations(range(1, N), i)}
        print(f"Length: {i:2d} | Number of combinations: ", len(current))
        
        for traveled in tqdm(current):

            for last_visited in traveled:
                if i == 1:
                    # Init
                    current[traveled][last_visited] = distance_matrix[0, last_visited]
                else:
                    # last_visited
                    citys = list(traveled)
                    citys.remove(last_visited)
                    current[traveled][last_visited] = min([previous[tuple(citys)][k]+distance_matrix[k, last_visited] for k in citys if k != last_visited])
        previous = current.copy()

    # len(comb) = 25
    return min([current[tuple([num for num in range(1, N)])][j]+distance_matrix[0, j] for j in range(1, N)])


def main():
    A = load_data('tsp.txt')
    distance_matrix = build_distance_matrix(A)
    tsp_ = tsp(distance_matrix)
    print("Answer is: ", int(tsp_))

if __name__ == '__main__':
    main()

from tqdm import tqdm
import numpy as np


def load_data(name):
    file = open(name,'r')
    data = file.readlines()
    
    n = int(data[0].split()[0])
    A = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j] = 0
            else:
                A[i,j] = np.inf
    for line in data[1:]:
        item = line.split()
        A[int(item[0]) -1 ,int(item[1])-1] = int(item[2])
        
    return A


def floyd_warshall(A):
    n = A.shape[0]
    previous = A
    current  = A

    # update n time
    for k in tqdm(range(n)):
        for i in range(n):
            current[:,i] = np.min([previous[:,i], previous[:,k]+previous[k,i]], axis=0)
        previous = current
    
    for i in range(n):
        if current[i,i] <0:
            min_path = 'Negative cycle'
            return min_path
    min_path = np.min(current)
    
    return min_path
    
    
def main():
    A = load_data('g1.txt')
    min_path = floyd_warshall(A)
    print(min_path)
    A = load_data('g2.txt')
    min_path = floyd_warshall(A)
    print(min_path)
    A = load_data('g3.txt')
    min_path = floyd_warshall(A)
    print(min_path)
    # -19

if __name__ == '__main__':
    main()
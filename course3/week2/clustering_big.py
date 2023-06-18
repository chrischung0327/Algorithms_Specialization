from tqdm.auto import tqdm

def load_data(name: str):
    f = open(name, "r")
    nodes = {tuple([int(y) for y in x.split()]): i for i, x in enumerate(f.readlines()[1:])}
    f.close()
    return nodes


def get_permutation(node):
    ret  = set()
    n    = len(node)
    node = list(node)
    # Two different
    for i in range(n):
        data = node.copy()
        data[i] = 1 if data[i] == 0 else 0
        ret.add(tuple(data))
        for j in range(i,n):
            tmp = data.copy()
            tmp[j] = 1 if tmp[j] == 0 else 0
            ret.add(tuple(tmp))
    return ret


def get_parent(i, parent):
    if parent[i] == i:
        return i
    else:
        return get_parent(parent[i], parent)


def merge(i, j, parent, cluster_size):
    i, j = get_parent(i, parent), get_parent(j, parent)
    if i != j:
        # prevent maximum recursion depth exceeded
        if cluster_size[i] > cluster_size[j]:
            parent[j] = i
        elif cluster_size[i] < cluster_size[j]:
            parent[i] = j
        else:
            parent[j] = i
            cluster_size[i] += 1


def main():
    nodes = load_data("clustering_big.txt")
    parent = {i: i for i in nodes}
    cluster_size = {i: 0 for i in nodes}

    for node in tqdm(nodes):
        for p in get_permutation(node):
            if p in parent:
                merge(node, p, parent, cluster_size)
       
    for node in nodes:
        parent[node] = get_parent(node, parent)
        
    print("Answer is: ", len(set(parent.values())))
    # 6118


if __name__ == '__main__':
    main()
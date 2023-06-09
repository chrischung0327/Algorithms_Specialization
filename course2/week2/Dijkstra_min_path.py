def parseFile(name):
    f = open(name, "r")
    lines = [x.split() for x in f.readlines()]
    f.close()
    nodes = {}
    for l in lines:
        nodes[int(l[0])] = l[1:]
    return nodes


def updateShortestPath(values, arr, info):
    shortest_path = float('inf')
    next_node = -1
    for x in info:
        i, length = [int(y) for y in x.split(',')]
        if arr[values] + length < arr[i]:
            arr[i] = arr[values] + length
            if arr[i] < shortest_path:
                shortest_path = arr[i]
                next_node = i

    return next_node




def runDijkstraAlgo(nodes: dict) -> list:
    arr = [float('inf')] * (len(nodes.keys())+1)
    arr[1] = 0
    visited = set()
    next_node = 1
    node_list = [1]
    # i = 0
    while next_node != -1 or len(node_list) > 1:
        if next_node != -1:
            node = next_node
        else:
            if len(node_list) == 0:
                break
            node = min(node_list,  key=lambda x: arr[x])
            
        visited.add(node)
        next_node = updateShortestPath(node, arr, nodes[node])
        node_list = [i for i, a in enumerate(arr) if (a != float('inf') and i not in visited)]

    return arr


def main():
    path = runDijkstraAlgo(parseFile('test_data.txt'))

    target = [7,37,59,82,99,115,133,165,188,197]
    for t in target:
        print(f"Shortest Path to node {t} is: {path[t]}")

    print("Answer is : ", ','.join([str(path[t]) for t in target]))


if __name__ == "__main__":
    main()

# 2599,2610,2947,2660,2367,2399,2029,2442,2505,3068

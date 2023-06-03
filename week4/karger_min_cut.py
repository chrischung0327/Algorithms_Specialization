import copy
import random


def readGraphFile(name: str):
    f = open(name, "r")
    lines = [x.split() for x in f.readlines()]
    f.close()
    graph = {}
    for line in lines:
        graph[line[0]] = line[1:]
    return graph


def random_pick(graph: dict):
    a = random.choice(list(graph.keys()))
    b = random.choice(list(graph[a]))
    return a, b


def kagerAlgo(graph: dict):
    while len(graph) > 2:
        node_a, node_b = random_pick(graph)
        graph[node_a] = graph[node_a] + graph[node_b]

        # remove all connection with node_b and add into node_a
        for node in graph[node_b]:
            graph[node].remove(node_b)
            graph[node].append(node_a)

        # remove self-loop in node_a
        while node_a in graph[node_a]:
            graph[node_a].remove(node_a)
        del graph[node_b]

    return len(graph[list(graph.keys())[0]])


def main(n:int, file: str):
    ret = float('inf')
    graph = readGraphFile(file)
    for _ in range(n):
        tmp = copy.deepcopy(graph)
        min_cut = kagerAlgo(tmp)
        if min_cut < ret:
            ret = min_cut
    return ret


print("Answer is: ", main(100, 'test_data.txt'))
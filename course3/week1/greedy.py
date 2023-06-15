def load_data(name: str):
    f = open(name, "r")
    lines = [x.split() for x in f.readlines()]
    length = int(lines[0][-1])
    for i in range(length):
        lines[i+1] = [int(x) for x in lines[i+1]]
    f.close()
    return lines[1:]


def main():
    # Load data
    raw = load_data("jobs.txt")

    # Question 1
    schedule = raw.copy()
    schedule.sort(key=lambda x: (x[0]-x[1], x[0]), reverse=True)
    cost, length = 0, 0
    for job in schedule:
        length += job[1]
        cost   += length*job[0]
    print("Answer of Q1: ", cost)

    # Question 2
    schedule = raw.copy()
    schedule.sort(key=lambda x: x[0]/x[1], reverse=True)
    cost, length = 0, 0
    for job in schedule:
        length += job[1]
        cost   += length*job[0]
    print("Answer of Q2: ", cost)

    # Queestion 3
    edge_raw = load_data("edges.txt")
    graph = {}
    for edge_info in edge_raw:
        vertex1, vertex2, edge_cost = edge_info
        if vertex1 in graph:
            graph[vertex1][vertex2] = edge_cost
        else:
            graph[vertex1] = {vertex2: edge_cost}
        if vertex2 in graph:
            graph[vertex2][vertex1] = edge_cost
        else:
            graph[vertex2] = {vertex1: edge_cost}

    unvisited = list(graph.keys())
    visited = set([unvisited.pop()])
    cost = 0
    while len(unvisited) > 0:
        vertex, edge_length = 0, 0
        for v1 in visited:
            potential_list = [v2 for v2 in graph[v1] if v2 not in visited]
            if len(potential_list) > 0:
                _vertex, _edge_length = min([[v2, graph[v1][v2]] for v2 in potential_list], key=lambda x: x[1])
                if vertex == 0 or _edge_length < edge_length:
                    vertex, edge_length =  _vertex, _edge_length

        cost += edge_length
        visited.add(vertex)
        unvisited.remove(vertex)
    print("Answer of Q3: ", cost)


if __name__ == '__main__':
    main()
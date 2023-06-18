def load_data(name: str):
    f = open(name, "r")
    lines = [x.split() for x in f.readlines()]
    graph = {}
    for i in range(1,len(lines)):
        # pair node a <-> node b: cost c
        a, b, c = lines[i]
        graph[(int(a), int(b))] = int(c)
    f.close()
    return graph


def main():

    graph = load_data("clustering1.txt")

    cluster = list(range(1, 501))
    number_of_cluster = 500


    while number_of_cluster > 4:
        edge = min(graph, key= lambda x: graph[x])
        cost = graph.pop(edge)
        p, q = cluster[edge[0]-1], cluster[edge[1]-1]
        if p != q and number_of_cluster > 4:
            number_of_cluster -= 1
            for i in range(500):
                # all q -> p, others remain the same
                cluster[i] = p if cluster[i] == q else cluster[i]
        elif p != q and number_of_cluster == 4:
            print(edge, p, q, cost)
            break


if __name__ == '__main__':
    main()
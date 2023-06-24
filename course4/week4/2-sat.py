def load_data(name):
    file = open(name, "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
    data = file.readlines()

    num_nodes = int(data[0])

    # Adjacency representations of the graph and reverse graph
    gr = {i: [] for i in range(-num_nodes, num_nodes+1)}
    r_gr = {i: [] for i in range(-num_nodes, num_nodes+1)}

    for line in data[1:]:
        items = line.split()
        gr[-int(items[0])] += [int(items[1])]
        gr[-int(items[1])] += [int(items[0])]
        r_gr[int(items[0])] += [-int(items[1])]
        r_gr[int(items[1])] += [-int(items[0])]

    return gr, r_gr, num_nodes 



def check_satisfication(name):
    gr, r_gr, num_nodes = load_data(name)

    visited = {i: False for i in range(-num_nodes, num_nodes+1)}

    scc = {i: set() for i in range(-num_nodes, num_nodes+1)}

    stack  = []  # Stack for DFS
    order  = []  # The finishing orders after the first pass
    finish = []
    finish_set = set()


    ########################################################
    # DFS on reverse graph

    for node in range(num_nodes-1, -1, -1):
        # print(node)
        if visited[node]:
            continue
        stack = [node]
        order = []
        i = 1
        while len(stack) > 0 or len(order) > 0:
            i += 1
            # if i % 40000 == 0:
                # print("Process: ", i)
                # print("s", len(stack), "o", len(order), "f", len(finish))
            # print("s", stack, "o", order, "f", finish)

            if len(stack) > 0:
                stack_node = stack.pop(-1)
                if visited[stack_node]:
                    continue
                visited[stack_node] = True
                flag = 0
                for head in r_gr[stack_node][::-1]:
                    if visited[head]:
                        continue
                    flag = 1
                    stack += head,
                if flag == 0:
                    # print(stack_node)
                    finish += stack_node,
                    finish_set.add(stack_node)
                else:
                    order += stack_node,

            else:
                stack_node = order.pop(-1) #[-1]
                # order = order[:-1]
                if stack_node not in finish_set:
                    # print(stack_node)
                    finish += stack_node,
                    finish_set.add(stack_node)


    # ########################################################
    # # DFS on original graph

    # print(finish)
    visited = {i: False for i in range(-num_nodes, num_nodes+1)}
    finish.reverse()  # The nodes should be visited in reverse finishing times
    sec_finish = set()
    # print()

    for node in finish:
        if visited[node]:
            continue
        stack = [node]
        scc[node].add(node)
        order = []
        back = 0
        while len(stack) > 0 or len(order) > 0:
            # print("s", stack, "o", order, "f", sec_finish)
            if len(stack) > 0:
                stack_node = stack.pop(-1)
                if visited[stack_node]:
                    continue
                visited[stack_node] = True
                flag = 0
                for head in gr[stack_node][::-1]:
                    if head == node:
                        back = 1
                    if visited[head]:
                        continue
                    flag = 1
                    # visited[head] = True
                    scc[node].add(head)
                    stack += head,
                if flag == 0:
                    sec_finish.add(stack_node)
                else:
                    order += stack_node,

            else:
                stack_node = order.pop(-1)
                if stack_node not in sec_finish:
                    sec_finish.add(stack_node)
        if back == 0:
            scc[node] = set([node])
        

    # print(scc)
    for s in scc:
        if len(scc[s]) > 1:
            for i in scc[s]:
                if i != 0 and -i in scc[s]:
                    print(scc[s], i)
                    print(f"File: {name} is: Not Satisfiable")
                    return '0'
    print(f"File: {name} is: Satisfiable")
    return '1'



def main():
    answer = [check_satisfication(f'2sat{x+1}.txt') for x in range(6)]
    print("Answer is: ", ''.join(answer))

if __name__ == '__main__':
    main()
import time

# Copyright David Bai: Anyone can use this code without permission or referencing the original source
"""
W1 Kosaraju Algorithm
List Based Iterative Implementation to find sizes of strongly connected components
---
The version is to implement in the basic limit of python
    - Not to extent # of recursive (if we use dfs func)
    - Not to change process memory usage 

In addition, I try to boost the program in to acceptable time
    - using tuple to append
    - using set to search if item already visited
"""

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
num_nodes = 875715

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack  = []  # Stack for DFS
order  = []  # The finishing orders after the first pass
finish = []
finish_set = set()


########################################################
# Importing the graphs
file = open("test_data.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

start = time.time()

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
            # stack = stack[:-1]
            if visited[stack_node]:
                continue
            visited[stack_node] = True
            flag = 0
            for head in r_gr[stack_node][::-1]:
                if visited[head]:
                    continue
                flag = 1
                # visited[head] = True
                # scc[head] = node
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


print(f"finish Step 1 with {time.time()-start}s")
# ########################################################
# # DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
finish.reverse()  # The nodes should be visited in reverse finishing times
result = []
# print(finish)
sec_finish = set()

for node in finish:
    if visited[node]:
        continue
    stack = [node]
    scc[node] = node
    order = []
    while len(stack) > 0 or len(order) > 0:
        # print("s", stack, "o", order, "f", sec_finish)
        if len(stack) > 0:
            stack_node = stack.pop(-1)
            if visited[stack_node]:
                continue
            visited[stack_node] = True
            flag = 0
            for head in gr[stack_node][::-1]:
                if visited[head]:
                    continue
                flag = 1
                # visited[head] = True
                scc[head] = node
                stack += head,
            if flag == 0:
                sec_finish.add(stack_node)
            else:
                order += stack_node,

        else:
            stack_node = order.pop(-1)
            if stack_node not in sec_finish:
                sec_finish.add(stack_node)
    
    
# ########################################################
# # Getting the five biggest sccs
# print(scc)
result = {}
for s in scc:
    if s not in result:
        result[s] = 1
    else:
        result[s] += 1

# print(result)
answer = sorted([v for _,v in result.items()])[::-1]
print(answer[:5])
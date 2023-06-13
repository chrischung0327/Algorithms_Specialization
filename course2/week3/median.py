class Node():
    def __init__(self) -> None:
        self.left  = None
        self.right = None
        self.value = None

class Heap():
    def __init__(self, method: str) -> None:
        self.method = method
        self.data   = [] 
        # parent's node: [-1, 0, 0, 1, 1, 2, 2 ,3, 3, ...]
        # node         : [0, 1(L), 2(R), ....]

    def get_peak(self):
        return self.data[0]
    
    def get_size(self):
        return len(self.data)
    
    def get_left_child(self, node):
        return node*2+1 if self.get_size()>(node*2+1) else None
    
    def get_right_child(self, node):
        return node*2+2 if self.get_size()>(node*2+2) else None
    
    def insert(self, value) -> None:
        self.data += value,
        self.sift_up(self.get_size()-1)
    
    def swap(self, left, right):
        self.data[left], self.data[right] = self.data[right], self.data[left]

    def extract(self):
        value = self.data.pop(0)
        plucked = self.data.pop(-1)
        self.data = [plucked] + self.data
        self.sift_down(0)
        return value
    
    def sift_up(self, node):
        if node == 0:
            return
        parent = (node-1) // 2
        value = self.data[parent]
        swap = None
        if node % 2 == 1:
            swap = node
        elif node % 2 == 0:
            if self.method == 'max':
                swap = node-1 if self.data[node-1] > self.data[node] else node
            elif self.method == 'min':
                swap = node-1 if self.data[node-1] < self.data[node] else node

        if swap:
            if (self.method == 'max' and self.data[swap] > value) or (self.method == 'min' and self.data[swap] < value):
                self.swap(parent, swap)
                self.sift_up(parent)

    def sift_down(self, node):
        value = self.data[node]
        left  = self.get_left_child(node)
        right = self.get_right_child(node)
        swap  = None

        if left and not right:
            swap = left
        elif left and right:
            if self.method == 'max':
                swap = left if self.data[left] > self.data[right] else right
            elif self.method == 'min':
                swap = left if self.data[left] < self.data[right] else right

        if swap:
            if (self.method == 'max' and self.data[swap] > value) or (self.method == 'min' and self.data[swap] < value):
                self.swap(node,swap)
                self.sift_down(swap)


class BinarySearchTree():
    # TODO
    def __init__(self) -> None:
        self.left  = None
        self.right = None
        self.value = None


def load_data(name: str):
    f = open(name, "r")
    lines = [int(x.strip()) for x in f.readlines()]
    f.close()
    return lines



def main():
    '''
    Mediam is the average of root of min-heap in greater side and root of max-heap in lower side
    '''
    # Load data
    raw = load_data("test_data.txt")

    # Init 
    min_heap = Heap(method='min')
    max_heap = Heap(method='max')
    median_list = []

    for i, value in enumerate(raw):
        # print(value)
        # choose to append in [min, max] heap
        if max_heap.get_size() > 0 and value > max_heap.get_peak():
            min_heap.insert(value)
        else:
            max_heap.insert(value)

        # Re-balance two heap
        if max_heap.get_size() > min_heap.get_size() + 1:
            temp = max_heap.extract()
            min_heap.insert(temp)
        
        if min_heap.get_size() > max_heap.get_size():
            temp = min_heap.extract()
            max_heap.insert(temp)

        median_list += max_heap.get_peak(),

        # if i in range(3040, 3050):
        #     print(i, value, f"Max:({max_heap.get_size()})", max_heap.data[:5], f'Min:({min_heap.get_size()})', min_heap.data[:10], max(max_heap.data), min(min_heap.data))
        # print('m', max_heap.data, 'M', min_heap.data) 

    print("Answer is: ", sum(median_list)%10000)

if __name__ == "__main__":
    main()

        






class Node:
    def __init__(self, s):
        self.data = s
        self.next = [None, None, None,None]


def build_tree():
    root = Node('red-1')
    root.next[0] = Node('orange-2')
    root.next[1] = Node('lime-3')
    root.next[2] = Node('green-4')
    root.next[0].next[0] = Node('yellow-5')
    root.next[2].next[0] = Node('blue-6')
    root.next[2].next[1] = Node('violet-7')
    root.next[0].next[0].next[0] = Node('purple-8')
    root.next[0].next[0].next[1] = Node('pink-9')
    root.next[0].next[0].next[2] = Node('black-10')
    root.next[0].next[0].next[3] = Node('brown-11')
    root.next[2].next[1].next[0] = Node('Gray-12')
    return root

Queue=[]
first=0
def bfs(start): #廣度
    global Queue ,first    
    if first == 0 :
        Queue.append(start)
        first=1
    for i in range(4):
        if start.next[i] is not None:
            Queue.append(start.next[i])
    data=Queue[0].data
    print(data, ' visited.')
    Queue.pop(0)
    if Queue==[]and first==1:
        return
    bfs(Queue[0])
    
def dfs(start): #深度
    if start is None:
        return
    print(start.data, ' visited.')
    for i in range(4):
        dfs(start.next[i])
    
tree = build_tree()
print('BFS')
bfs(tree)
print('\nDFS')
dfs(tree)
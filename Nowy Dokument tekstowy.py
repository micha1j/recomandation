from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.depth = 0
    def add_child(self, child):
        self.children.append(child)
        child.depth = self.depth +1
    def get_value(self):
        return self.value
def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the  frontier
    for child in current_node.children:
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add_node(self, new_node, current_node_value=None):
        print(new_node, current_node_value)
        if current_node_value == None:
            if self.head == None:
                self.head = new_node
                return
            else:
                current_node_value = input("Which category should thiss be?: ")
        
        curenode=bfs(self.head, current_node_value)[-1]
        if curenode == None:
            return
        curenode.add_child(new_node)
        self.size +=1
    def show(self):
        print("Showing...")
        nodes_to_visit = [self.head]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            for x in range(current_node.depth):
                print("|", end="")
           
            print(current_node.value)
            nodes_to_visit += current_node.children
 
lista = LinkedList() 
z = Node(0)
lista.add_node(z)
com = Node("Polskie")
lista.add_node(com, 0)
oko = Node("Amerykańskie")
lista.add_node(oko, 0)
wiedzmin = Node("Wiedźmin")
lista.add_node(wiedzmin, "Polskie")
cuberpunk = Node("Cyberpunk")
lista.add_node(cuberpunk, "Polskie") 
#lista.show()
print("Skąd chcesz sprawdzić genry?")
current_node = lista.head
for x in current_node.children:
    print(x.value)
inpu1 = input("Wpisz genre: ")
xsom = []
for x in current_node.children:
    xsom.append(x.value)
while True:
    if inpu1 in xsom:
        break
    for x in current_node.children:
        print(x.value)
    inpu1 = input("Wpisz genre: ")
    print(x)
current_node = bfs(current_node, inpu1)[-1]
print("Możliwośći")
print("")
for x in current_node.children:
    print(x.value)         
          
          







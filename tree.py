class Node(object):

  def __init__(self, value, left_child = None, right_child = None):
    self.value = value
    self.left = left_child
    self.right = right_child
    self.visited = False

  def visit(self):
    print(self.value, end = " ")
    self.visited = False

def inorder(node: Node):
  if node is not None:
    inorder(node.left)
    node.visit()
    inorder(node.right)

def preorder(node: Node):
  if node is not None:
    node.visit()
    preorder(node.left)
    preorder(node.right)

def postorder(node: Node):
  if node is not None:
    postorder(node.left)
    postorder(node.right)
    node.visit()


def main():
  inputs = [
    Node(8,
      Node(4,
        Node(2),
        Node(6)
      ),
      Node(10,
        None,
        Node(20)
      )
    ),
    Node(10,
      Node(5,
        Node(3),
        Node(7)
      ),
      Node(20,
        None,
        Node(30)
      )
    ),
  ]
  for root_node in inputs:
    print("Inorder:", end = " ")
    inorder(root_node)
    print()
    
    print("Pre-order:", end = " ")
    preorder(root_node)
    print()
    
    print("Post-order:", end = " ")
    postorder(root_node)
    print()
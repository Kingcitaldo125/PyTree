from tree.tree import Tree, Node

tree = Tree(Node(8))
root = tree.getRoot()

print("Root:", root)

print("Traverse before add")
tree.traverse(tree.getRoot())

tree.addNode(Node(5), root)
tree.addNode(Node(13), root)
tree.addNode(Node(3), root)
tree.addNode(Node(6), root)
tree.addNode(Node(12), root)
tree.addNode(Node(16), root)

print("Traverse after add(s)")
tree.traverse(tree.getRoot())

print("Has Node 4", tree.hasNode(Node(4), root))
print("Has Node 5", tree.hasNode(Node(5), root))

#tree.render_graph()

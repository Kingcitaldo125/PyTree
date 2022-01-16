import graphviz

from tree.node import Node

class Tree(object):
    """
    Binary search tree
    """

    def __init__(self, node:Node):
        self.rootNode = node
        self.dot = graphviz.Digraph(comment='My Tree')

    def __constructGraphNode(self, node):
        self.dot.node(node.getContentStr())

    def __constructGraphNodeEdge(self, node, child):
        self.__constructGraphNode(child)
        self.dot.edge(node.getContentStr(), child.getContentStr())

    def __traverse(self, node, construct_graph, print_visit):
        if construct_graph:
            self.__constructGraphNode(node)

        if node.hasLeftChild():
            if construct_graph:
                self.__constructGraphNodeEdge(node, node.left)

            self.__traverse(node.left, construct_graph, print_visit)

        if print_visit:
            print(f"Visited node '{node}'")

        if node.hasRightChild():
            if construct_graph:
                self.__constructGraphNodeEdge(node, node.right)

            self.__traverse(node.right, construct_graph, print_visit)

    def traverse(self, node, construct_graph=False, print_visit=True):
        """
        In-order traversal
        """

        self.__traverse(node, construct_graph, print_visit)

    def addNode(self, node: Node, root: Node):
        rootVal = root.getContent()
        nodeVal = node.getContent()

        if nodeVal <= rootVal:
            if not root.hasLeftChild():
                root.left = node
                return
            self.addNode(node, root.left)
        else:
            if not root.hasRightChild():
                root.right = node
                return
            self.addNode(node, root.right)

    def hasNode(self, node: Node, root: Node):
        nodeVal = node.getContent()
        rootVal = root.getContent()

        if nodeVal == rootVal:
            return True

        if nodeVal <= rootVal:
            if root.hasLeftChild():
                return self.hasNode(node, root.left)
            return False
        else:
            if root.hasRightChild():
                return self.hasNode(node, root.right)
            return False

    def getRoot(self):
        return self.rootNode

    def getMin(self, node:Node):
        if not node.hasLeftChild():
            return node

        return self.getMin(node.left)

    def getMax(self, node:Node):
        if not node.hasRightChild():
            return node

        return self.getMax(node.right)

    def render_graph(self, view=True):
        self.dot = graphviz.Digraph(comment='My Tree')

        self.__traverse(self.rootNode, True, False)

        self.dot.render('renderedtree/graph.gv', view=view)

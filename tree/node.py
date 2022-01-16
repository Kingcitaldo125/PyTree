class Node(object):
    """
    Binary search tree Node: Single element in a BST
    """

    def __init__(self, content):
        self.left = None
        self.right = None
        self.content = content

    def __str__(self):
        return str(self.content)

    def getContent(self):
        return self.content

    def getContentStr(self):
        return str(self.content)

    def hasLeftChild(self):
        return self.left != None

    def hasRightChild(self):
        return self.right != None

    def hasChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

# 每个节点都是BinaryTree类的一个实例
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        '''现有leftChild为None, 或存在'''
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.leftChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key

    # 前序遍历作为类的方法
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


# 树的遍历
# 前序遍历
def preorder(tree):
    '''先访问根节点，然后依次递归地前序遍历左子树和右子树'''
    if tree:
        print(tree.getRootvalue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# 后序遍历
def postorder(tree):
    '''先遍历左右子树， 然后访问根节点'''
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootvalue)


# 中序遍历
def inorder(tree):
    '''先递归遍历左子树，然后访问根节点， 最后递归遍历右子树'''
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootvalue())
        inorder(tree.getRightChild())


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    print(r.getRootValue())
    print(r.getLeftChild())     # BinaryTree的一个实例
    print(r.getRightChild())
    print(r.getLeftChild().getRootValue())
    print(r.getRightChild().getRootValue())
    r.getRightChild().setRootValue('hello')
    print(r.getRightChild().getRootValue())

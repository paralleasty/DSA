import operator
from pythonds import Stack
from tree import BinaryTree


# 跟踪当前节点和它的父节点
def buildParseTree(fpexp):
    '''
    1.If the current token is a '(', add a new node as the left child of
      the current node, and descend to the left child.
    2.If the current token is in the list ['+','-','/','*'], set the root
      value of the current node to the operator represented by the current
      token. Add a new node as the right child of the current node and
      descend to the right child.
    3.If the current token is a number, set the root value of the current
      node to the number and return to the parent.
    4.If the current token is a ')', go to the parent of the current node.
    '''
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootValue(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootValue(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    # 获取对当前节点的左右子节点的引用
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()

    # 没有子节点，即为叶节点，是基本情况
    if leftChild and rightChild:
        fn = opers[parseTree.getRootValue()]
        return fn(evaluate(leftChild), evaluate(rightChild))
    else:
        return parseTree.getRootValue()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")

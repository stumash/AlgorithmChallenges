import sys

def main():
    input_list = eval(sys.argv[1])
    root = parseTreeFromList(input_list)

    printTree(root, 0)
    flatten(root)
    printDoublyLinkedList(root)

def flatten(root):
    oldLeft, oldRight = root.left, root.right
    root.left, root.right = None, None

    if oldLeft != None:
        flatten(oldLeft)
        root.right = oldLeft
        # root.right.left = root # uncomment this line for doubly-linked list!
    if (oldRight != None):
        end = endOfList(root)
        flatten(oldRight)
        end.right = oldRight
        # oldRight.left = end # uncomment this line for doubly-linked list!

def endOfList(head):
    while head.right != None:
        head = head.right
    return head


# TESTING INFRASTRUCTURE
# ==============================

class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def parseTreeFromList(l):
    nodes = [TreeNode(l[i]) for i in range(len(l))]
    for i in range(len(nodes)):
        if i*2 + 1 < len(nodes):
            nodes[i].left = nodes[i*2 + 1]
        if i*2 + 2 < len(nodes):
            nodes[i].right = nodes[i*2 + 2]
    if nodes != []:
        return nodes[0]
    else:
        raise Error("need non-empty python list as argument")

def printTree(node, depth):
    indent = "    " * depth
    val = "-" if node == None else node.val
    print(indent + str(val))

    if (node != None):
        printTree(node.left, depth+1)
        printTree(node.right, depth+1)

def printDoublyLinkedList(head):
    while head != None:
        left = "None" if head.left == None else str(head.left.val)
        left = left.ljust(5)
        val = head.val
        right = "None" if head.right == None else str(head.right.val)
        right = right.rjust(5)
        print("{} <-- {} --> {}".format(left, val, right))

        head = head.right


if __name__ == "__main__":
    main()

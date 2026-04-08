import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def tree_insert(root, value):
    if root is None:
        return TreeNode(value)

    current = root

    while True:
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(value)
                break
            current = current.right

    return root



def level_order(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result



def depth_paths(root):
    if root is None:
        return []

    stack = [(root, [root.value])]
    paths = []

    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            paths.append(path)

        if node.right is not None:
            stack.append((node.right, path + [node.right.value]))
        if node.left is not None:
            stack.append((node.left, path + [node.left.value]))

    return paths



def main():
    print("\n========== QUESTAO 5 ==========")
    values = random.sample(range(1, 50), 10)
    root = None

    for value in values:
        root = tree_insert(root, value)

    print("inserted values:", values)
    print("level order (BFS):", level_order(root))
    print("paths from root to leaves (DFS):")
    for path in depth_paths(root):
        print(path)


if __name__ == "__main__":
    main()

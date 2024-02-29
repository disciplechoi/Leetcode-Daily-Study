class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)


# 예제 사용
bt = BinaryTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bt.insert(key)

search_key = 60
result_node = bt.search(search_key)

if result_node:
    print(f"값 {search_key}을(를) 찾았습니다.")
else:
    print(f"값 {search_key}을(를) 찾을 수 없습니다.")

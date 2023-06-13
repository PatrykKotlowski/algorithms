class BST:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value: int):
        if self.value is None:
            self.value = value
            return
        if self.value == value:
            return

        if value < self.value:
            if self.left is None:
                self.left = BST(value=value)
                return
            self.left.insert(value)
            return
        if self.right is None:
            self.right = BST(value=value)
            return
        self.right.insert(value)

    def preorder(self, values: list):
        if self.value is not None:
            values.append(self.value)
            #values.insert(0, self.value)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)

    def inorder(self, values: list):
        if self.left is not None:
            self.left.inorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right.inorder(values)

    def postorder(self, values: list):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        if self.value is not None:
            values.append(self.value)

    def get_min(self):
        if self is None:
            return
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node.value

    def get_max(self):
        if self is None:
            return
        curr_node = self
        while curr_node.right is not None:
            curr_node = curr_node.right
        return curr_node.value

    def delete(self, value):
        if self.value is None:
            return
        if value < self.value:
            self.left.delete(value)
        elif value < self.value:
            self.right.delete(value)
        else:
            if self.left is None:
                self.value = None
                return self.right
            if self.right is None:
                self.value = None
                return self.left

            inorder_succesor = self.right.get_min()
            self.value = inorder_succesor.value
            self.right = inorder_succesor.delete(value)

            return self


if __name__ == '__main__':
    #nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    nums = [22, 12, 30, 8, 20, 25, 40]
    bst = BST()
    for num in nums:
        bst.insert(num)

    funcs = (
        (bst.preorder, [22, 12, 8, 20, 30, 25, 40]),
        (bst.postorder, [8, 20, 12, 25, 40, 30, 22]),
        (bst.inorder, [8, 12, 20, 22, 25, 30, 40])
    )
    for func, wanted in funcs:
        vals = []
        func(vals)
        assert wanted == vals, f"{vals} {func.__name__}"
        print(func.__name__, vals)

    assert bst.get_min() == 8
    assert bst.get_max() == 40


    nums = [50, 30, 20, 40, 70, 60, 80]
    bst = BST()
    for num in nums:
        bst.insert(num)

    bst.delete(20)

    funcs = (
        (bst.inorder, [30, 40, 50, 60, 70, 80]),
    )
    for func, wanted in funcs:
        vals = []
        func(vals)
        assert wanted == vals, f"{vals} {func.__name__}"
        print(func.__name__, vals)

    
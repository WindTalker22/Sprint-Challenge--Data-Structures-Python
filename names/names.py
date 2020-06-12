import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        # First we check if the new value is less than the initial instances value
        if value < self.value:
            # We then check if the initial instances left pointer is equal to None
            if self.left is None:
                # If it is we then instantiate a new instance and set the initial instances left pointer to the new instance
                self.left = BSTNode(value)
            else:
                # We hop over the node that the instance is pointing to and insert new node recursively
                self.left.insert(value)
        else:
            # If the value of the instance was greater
            # We then check if the  instances right pointer is equal to None
            if self.right is None:
                # If it is we then instantiate a new instance and set the initial instances right pointer to the new instance
                self.right = BSTNode(value)
            else:
                # We hop over the node that the instance is pointing to and insert new node recursively
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # If initial instance value is the same as the new value return true
        if self.value is target:
            return True
        # We then decide which direction to traverse down the tree
        # If this is true we go left and check the values
        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
        # If this is true we go right and check the values
        elif self.value < target:
            if self.right is not None:
                return self.right.contains(target)
        else:
            # If neither of the previous conditions are met we return False
            return False


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
bst = BSTNode("")


# <------STRETCH------->
# Set and Intersect
# I believe this is O(1)
# runtime: 0.004808902740478516 seconds
# duplicates = list(set(names_1).intersection(set(names_2)))

# <------STRETCH------->
# List comprehension
# I believe this is O(log n)
# runtime: 1.2950398921966553 seconds
# duplicates = [name for name in names_1 if name in names_2]


# Binary Search Tree
# I believe this is O(n)
# runtime: 0.1267399787902832 seconds
for name in names_1:
    bst.insert(name)


for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
binarySearchTree = None

for nameOne in names_1:
    if binarySearchTree is None:
        binarySearchTree = BinarySearchTree(nameOne)
    else:
        binarySearchTree.insert(nameOne)
for nameTwo in names_2:
    if binarySearchTree.contains(nameTwo):
        duplicates.append(nameTwo)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


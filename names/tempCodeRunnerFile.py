for name in names_1:
    bst.insert(name)


for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

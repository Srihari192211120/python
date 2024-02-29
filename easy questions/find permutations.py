from itertools import permutations
def unique_permutations(num):
    perms = permutations(num)
    unique_perms  = set()
    for perm in perms:
        perm_str = "".join(perm)
        unique_perms .add(perm_str)
    for perm in unique_perms:
        print(perm)

num = input("enter a number: ")
unique_permutations(num)

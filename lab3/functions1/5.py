from itertools import permutations
def perm(string):
    permutation = [''.join(i) for i in permutations(string)]
    for i in permutation:
        print(i)
perm(input())
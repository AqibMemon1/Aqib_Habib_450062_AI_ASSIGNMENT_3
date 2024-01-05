# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations


N=int(input())
M=list(input().split(" "))
L=int(input())
K=list(combinations(M, L))
container= [i for i in K if "a" in i]
print(len(container)/len(K))
    



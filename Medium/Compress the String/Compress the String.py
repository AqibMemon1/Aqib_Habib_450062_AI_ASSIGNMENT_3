# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
str_in=input()

for k, c in groupby(str_in):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
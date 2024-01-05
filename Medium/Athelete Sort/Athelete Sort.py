import math
import os
import random
import re
import sys
N, M = map(int, input().split())
rows=[]
for _ in range(N):
    rows.append(input())
K = int(input())
for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)
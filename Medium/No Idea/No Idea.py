# Enter your code here. Read input from STDIN. Print output to STDOUT

happiness = 0

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
good_bhai = set(map(int, input().split(' ')))
bad_bhai = set(map(int, input().split(' ')))
    
for i in arr:
    if i in good_bhai:
        happiness += 1
    elif i in bad_bhai:
        happiness -= 1
print(happiness)
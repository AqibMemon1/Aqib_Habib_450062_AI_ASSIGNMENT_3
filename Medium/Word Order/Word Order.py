from collections import Counter
N = int(input())
words = []
for i in range(N):
    words.append(input().strip())
count = Counter(words)
print(len(count))
print(*count.values())
import sys

n = int(sys.stdin.readline())
result = list(sys.stdin.readline().rstrip())
total= 0
for i in range(n):
  total += int(result[i])

print(total)
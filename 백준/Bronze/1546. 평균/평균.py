N = int(input())
sub = list(map(int, input().split()))
M = max(sub)
sum = sum(sub)
print(sum * 100 / M / N)
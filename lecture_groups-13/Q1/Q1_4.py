# 解説確認後
n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
found = [False]*n

ans = 0
for j in range(m):
	for i in range(n):
		if found[i]:
			continue
		if A[i] <= B[j]:
			found[i] = True
			ans += 1
			break
print(ans)
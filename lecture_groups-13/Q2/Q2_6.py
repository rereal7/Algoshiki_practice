# Q2-6. 重さは何番目？

n = int(input())
W = list(map(int, input().split()))

W_sorted = sorted(W)

for i in range(n):
	left = -1
	right = n
	while right - left > 1:
		mid = (right + left) // 2
		if W_sorted[mid] <= W[i]:
			left = mid
		else:
			right = mid
	print(left)
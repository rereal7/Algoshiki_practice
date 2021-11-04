# Q2-4. 小さい数の個数

n,m = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()

for i in range(m):
	left = 0
	right = n
	while left != right:
		mid = (left + right) // 2
		if A[mid] > B[i]:
			right = mid
		else:
			left = mid+1 # indexを考慮して+1
	print(left)
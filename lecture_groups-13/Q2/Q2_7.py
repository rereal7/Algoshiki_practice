# Q2-7. 貯金 (2)

# Q2-2の類題

def f(x):
	return x*(x+1)/2

n = int(input())
X = list(map(int, input().split()))

for i in range(n):
	left = 0
	right = 2*(10**9) # f(2*(10**9))は十分に範囲外
	while right != left:
		mid = (right+left)//2
		if f(mid) >= X[i]:
			right = mid
		else:
			left = mid+1
	print(left)
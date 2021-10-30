# Q2-1. 方程式を解く
n = int(input())

left = 0
right = 100
while right - left > 1e-4:
	mid = (right + left) / 2
	f = ((mid+1)*mid +2)*mid + 3
	if f < n:
		left = mid
	else:
		right = mid

ans = left 
print(ans)
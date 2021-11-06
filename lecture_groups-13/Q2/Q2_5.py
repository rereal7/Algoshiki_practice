# Q2-5. 和が K 以上のペア

# Q2-4 の類題
# 変数i,jを同時に探索するのは現実的ではないので、変数iを固定して全探索し
# 変数jを２分探索することで、十分高速になる。
# 片側を固定して、もう片方を全探索する手法はよく見る気がする。

n,k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

count = 0
for i in range(n):
	left = 0
	right = n
	while left != right:
		mid = (left + right)//2
		if A[mid] >= k - A[i]:
			right = mid
		else:
			left = mid + 1
	count += n - left
print(count)
x = int(input())
A = list(map(int, input().split()))
C = [50, 10, 5, 1]

ans = 0
for i in range(4):
	for j in range(A[i]):
		# 手持ちの金額が対象の硬貨よりも少ない場合はスキップ
		if x < C[i]:
			break
		else:
			x -= C[i]
			ans += 1

print(ans)

# 解説確認後
x = int(input())
A = list(map(int, input().split()))
C = [50, 10, 5, 1]

ans = 0
for i in range(4):
	# 手持ちの硬貨の枚数を考えない最大の枚数
	add = x//C[i]

	# 実際の手持ちの枚数を考慮する
	add = min(add, A[i])
	ans += add

	# 使った硬貨の枚数分の金額を減らす
	x -= C[i]*add

print(ans)
